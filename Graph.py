class Graph:
    def __init__(self):
        self.items = []
        self.adj_matrix = []
        self.num_items = 0
    def add_item(self, item):
        self.items.append(item)
        print(f"adj matrix is {self.adj_matrix}")
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
    #def get_num_of_