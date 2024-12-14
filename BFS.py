class Graph:
    def __init__(self):
        self.data = {}

    def add_edge(self, node1, node2):
        if node1 not in self.data:
            self.data[node1] = []
        if node2 not in self.data:
            self.data[node2] = []
        self.data[node1].append(node2)
        self.data[node2].append(node1)

    def __repr__(self):
        return f"Graph(data={self.data})"
    
    def __str__(self):
        result = "Graph adjacency list:\n"
        for node, adjacent_nodes in self.data.items():
            result += f"{node}: {adjacent_nodes}\n"
        return result

