#Basic undirected graph

class Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = []

        for i in range(0, size):
            self.nodes.append(  [])
            for j in range(0, size):
                self.nodes[i].append(0)

    def get_adjacency_arr(self):
        return self.nodes

    def __str__(self):
        actual_str = ""
        char = ""

        for i in range(0, self.size):
            actual_str += "["
            for j in range(0, self.size):
                char = ", " if j != self.size - 1 else ""
                actual_str += str(self.nodes[i][j]) + char
            actual_str += "]\n"

        return actual_str

    def display_connections(self):
        actual_str = ""

        for i in range(0, self.size):
            actual_str += f"Node_{i} is connected to: "
            for j in range (0, self.size):
                if self.nodes[i][j]:
                    actual_str +=  f"Node_{j} "
            actual_str += "\n"

        return actual_str

    def add_edge(self, a: int, b: int):
        if 0 <= a < self.size and 0 <= b < self.size:
            self.nodes[a][b] = 1
            self.nodes[b][a] = 1

a = Graph(5)
a.add_edge(0, 1)
a.add_edge(0, 2)
a.add_edge(0, 3)
a.add_edge(1, 4)
a.add_edge(2, 5)

print(a)
print(a.display_connections())