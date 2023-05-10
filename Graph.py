class Graph:
    def __init__(self):
        self.items = []
        self.adj_matrix = []
        self.num_items = 0
    def add_item(self, item):
        self.items.append(item)
        # print(f"adj matrix is {self.adj_matrix}")
        for arr in self.adj_matrix:
            arr.append(0)
        new_line = [0 for i in range(self.num_items)]
        new_line.append(-1)
        self.adj_matrix.append(new_line)
        self.num_items += 1
    def remove_item(self, item):
        if not self.is_item_in_graph(item):
            raise ValueError (f"Cannot remove {item}; it is not in graph")
        item_index = self.get_item_index(item)
        for arr in self.adj_matrix:
            arr.pop(item_index) # removes at index
        self.adj_matrix.pop(item_index) # removes its row
    def get_item_index(self, item):
        try:
            return self.items.index(item)
        except ValueError:
            print(f"Oops: {item} not in graph")
            return -1
    def is_item_in_graph(self, item):
        return item in self.items
    def add_link(self, item1, item2, weight):
        if weight < 0:
            raise ValueError("Cannot add link between {item1} and {item2}: weight must be >= 0")
        index1 = self.get_item_index(item1)
        index2 = self.get_item_index(item2)
        self.adj_matrix[index1][index2] = weight
        self.adj_matrix[index2][index1] = weight
    def num_links_of_item(self, item):
        num_links = 0
        index = self.get_item_index(item)
        for val in self.adj_matrix:
            if val > 0:
                num_links += 1
    def get_connected_devices(self, item):
        connect_devices = []
        index = self.get_item_index(item)
        for i in range(len(self.adj_matrix[index])):
            link_val = self.adj_matrix[index][i]
            if link_val > 0:
                connect_devices.append(self.items[i])
        return connect_devices
    # def get_dijkstra(self, item):
    #     # the shoddiest dijkstra you've ever seen
    #     hosts_visited = []
    #     hosts_to_visit = []
    #     distance_matrix = [float('inf') for i in range(len(self.adj_matrix[0]))]
    #     print(total_path_matrix)
    #     next_node_matrix = []
    #     starting_index = self.graph.get_item_index(item)
    #     current_index = starting_index
    #     while (not all(item in hosts_visited for item in self.items)):
    #         connected_devices = self.get_connected_devices(self.items[current_index])
    #         for device in connected_devices:
    #             new_device_index = self.graph.get_item_index(device)
    #             len_from_current_device_to_new_device = self.items[current_index][new_device_index]
    #             total_proposed_len = distance_matrix[new_device_index] + len_from_current_device_to_new_device
    #             if total_proposed_len < distance_matrix[new_device_index]:
    #                 distance_matrix[new_device_index] = total_proposed_len


    # def get_dijstra_helper(self, item):
        pass
    # def dijkstra(self, start_node):
    #     start = self.get_item_index(start_node)
    #     visited = [start]
    #     n = len(self.items)
    #     distances = {i: float('inf') for i in range(n)}
    #     distances[start] = 0
        
    #     while len(visited) < n:
    #         current = min(visited, key=lambda x: distances[x])
            
    #         for neighbor in range(n):
    #             if self.adj_matrix[current][neighbor] != -1:
    #                 distance = distances[current] + self.adj_matrix[current][neighbor]
    #                 if distance < distances[neighbor]:
    #                     distances[neighbor] = distance
    #                     visited.append(neighbor)
    #             print(f"distances while on node {current}: {distances}")
        
    #     return distances
    def dijkstra(self, start):
        visited = [start]
        n = len(self.items)
        distances = {i: float('inf') for i in range(n)}
        distances[start] = 0
        
        while len(visited) < n:
            current = min([x for x in visited if x != current], key=lambda x: distances[x])
            print(f"in current {current}")
            for neighbor in range(n):
                print(f"in neighbor {neighbor}")
                if self.adj_matrix[current][neighbor] != 0 and self.adj_matrix[current][neighbor] != -1:
                    distance = distances[current] + self.adj_matrix[current][neighbor]
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
            
            next_nodes = [node for node in range(n) if node not in visited and distances[node] != float('inf')]
            if not next_nodes:
                break
            next_node = min(next_nodes, key=lambda x: distances[x])
            visited.append(next_node)
        
        return distances
