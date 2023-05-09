import sys
from Network import Network

LOG_FILE_NAME = "log.txt"
HOST_FILE_NAME = "ips.txt" 


def main(argv):
    network = Network("log.txt", "ips.txt")
    pass

if __name__ == "__main__":
    argv = sys.argv
    main(argv)
