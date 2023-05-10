import sys
from Network import Network
import random

LOG_FILE_NAME = "log.txt"
HOST_FILE_NAME = "ips.txt"
CONNECTION_FILE_NAME = "connection.txt"
MAX_TIME = 100
ABSOLUTE_MAX_TIME = 110
PERCENT_OF_SENDING = .05
PERCENT_OF_FAILURE = .01

def main(argv):
    network = Network("log.txt", "ips.txt", "connections.txt")
    time = 0
    while time < ABSOLUTE_MAX_TIME:
        if time <= MAX_TIME:
            for device in network.graph.items:
                if random.random() <= PERCENT_OF_SENDING:
                    # send a packet to a random connected 
                    network.send_packet_to_random_connected_device(device, "Here is the data", time)
                if random.random() <= PERCENT_OF_FAILURE:
                    network.log(f"{time}: {device} failed... MAIN\n")
        time += 1
    print(network.graph.dijkstra(0))


if __name__ == "__main__":
    argv = sys.argv
    main(argv)
