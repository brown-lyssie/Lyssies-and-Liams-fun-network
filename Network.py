from Graph import Graph

class Network:
    def __init__(self, log_file_name: str, host_file_name: str):
        self.log_file_name = log_file_name
        self.host_file_name = host_file_name
        self.graph = Graph()
        self.clear_log_file()
        self.packets_in_motion = [] # tuple: (data, source_ip, destination_ip, time_left)
        # ~~~
        self.log(f"Adding devices from {host_file_name}...")
        self.setup_devices() 
    def clear_log_file(self):
        with open(self.log_file_name, "w"):
            pass
    def setup_devices(self):
        # insert new devices
        with open(self.host_file_name, "r") as hf: # will throw error if no host file
            lines = hf.readlines()
        clean_lines = []
        for line in lines:
            clean_lines.append(line.strip())
        print(clean_lines)
        for line in clean_lines:
            self.add_device(line)
       
    def log(self, str, indent = 0):
        with open(self.log_file_name, "a") as f:
            f.write("\t" * indent + str)
    def add_device(self, ip: str):
        self.graph.add_item(ip)
        self.log(f"Device with IP address of {ip} added to network. \n", indent = 1)
    def connect_devices(self, ip1: str, ip2: str, weight):
        self.graph.add_link(ip1, ip2, weight)
        self.log(f"Hosts with ips {ip1} and {ip2} linked with weight {weight}")