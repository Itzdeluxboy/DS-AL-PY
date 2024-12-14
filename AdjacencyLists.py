class Graph:
    def __init__(self):
        self.adj_list={}

    def add_edge(self, node1, node2):
        if node1 not in self.adj_list:
            self.adj_list[node1]=[]
        self.adj_list[node1].append(node2)

        if node2 not in self.adj_list:
            self.adj_list[node2]=[]
        self.adj_list[node2].append(node2)

    def __repr__(self):
        return f"Graph(adj_list={self.adj_list})"
    
    def __str__(self):
        result = "Graph adjacency list:\n"
        for node, nxt_node in self.adj_list.items():
            result+= f"{node}: {nxt_node}\n"
        return result
    
    def display(self):

        print(self)

graph = Graph()

graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.display()
print(repr(graph))