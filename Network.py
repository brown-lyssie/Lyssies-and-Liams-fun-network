import queue
from Graph import Graph
import random

class Network:
    def __init__(self, log_file_name: str, host_file_name: str, link_file_name: str):
        self.queue = queue.PriorityQueue()
        self.log_file_name = log_file_name
        self.host_file_name = host_file_name
        self.link_file_name = link_file_name
        self.graph = Graph()
        self.clear_log_file()
        self.packets_in_motion = [] # tuple: (data, source_ip, destination_ip, time_left)
        # ~~~
        
        self.setup_devices()
    def clear_log_file(self):
        with open(self.log_file_name, "w"):
            pass
    def setup_devices(self):
        
        # insert new devices
        with open(self.host_file_name, "r") as hf: # will throw error if no host file
            hflines = hf.readlines()
        hf_clean_lines = []
        for hfline in hflines:
            hf_clean_lines.append(hfline.strip())
        # print(hf_clean_lines)
        self.log(f"Adding devices from {self.host_file_name}...")
        for hfcline in hf_clean_lines:
            self.add_device(hfcline)
        with open(self.link_file_name, "r") as lf: # will throw error if no link file
            lflines = lf.readlines()
        lf_clean_lines = []
        for lfline in lflines:
            lf_clean_lines.append(lfline.strip())
        self.log(f"Connecting devices from {self.link_file_name}...\n")
        for lfcline in lf_clean_lines:
            split_vals = lfcline.split()
            self.connect_devices(split_vals[0], split_vals[1], int(split_vals[2]))
            self.log(f"Added link with weight {split_vals[2]} between hosts with ips {split_vals[0]} and {split_vals[1]}.\n", indent =1)
        print(self.graph.adj_matrix)
    def log(self, str, indent = 0):
        with open(self.log_file_name, "a") as f:
            f.write("\t" * indent + str)
    def add_device(self, ip: str):
        self.graph.add_item(ip)
        self.log(f"Device with IP address of {ip} added to network. \n", indent = 1)
    def connect_devices(self, ip1: str, ip2: str, weight):
        self.graph.add_link(ip1, ip2, weight)
        # self.log(f"Hosts with ips {ip1} and {ip2} linked with weight {weight}\n")
    def send_out_packet(self, ip1: str, ip2: str, data: str, current_time: int):
        index1 = self.graph.get_item_index(ip1)
        index2 = self.graph.get_item_index(ip2)
        link_len = self.graph.adj_matrix[index1][index2]
        print(f"link val beween {ip1} and {ip2} is {link_len}")
        if (link_len <= 0):
            raise ValueError (f"Cannot send out packet: Hosts with ips {ip1} and {ip2} are not linked")
        arrival_time = current_time + link_len
        self.queue.put( (arrival_time, ip2, data) )
        self.log(f"{current_time}: Host with ip {ip1} sent out a packet to host with ip {ip2}. It will arrive at time {arrival_time}.\n")
    def handle_packet_arrival(self, arrival_time, ip2, data):
        self.log("Packet arrived at {ip2}. It comtained the following data:")
        self.log(data, indent = 2)
    def send_packet_to_random_connected_device(self, ip1: str, data: str, current_time: int):
        connect_devices = self.graph.get_connected_devices(ip1)
        rand_host_num = int(random.uniform(0, len(connect_devices) - 1))
        ip2 = connect_devices[rand_host_num]
        self.send_out_packet(ip1, ip2, data, current_time)