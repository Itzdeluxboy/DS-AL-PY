class GraphMatrix:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        #the below code makes it so that the matrix is filled with zeros
        self.adj_matrix = [[0]* num_nodes for _ in range(num_nodes)]

    def add_edge(self, node1, node2):
        self.adj_matrix[node1][node2] = 1
        self.adj_matrix[node2][node1] = 1

    def __repr__(self):

        return f"GraphMatrix(num_nodes={self.num_nodes}, adj_matrix={self.adj_matrix})"

    def __str__(self):
        
        result = 'Adjacency Matrix:\n'
        for row in self.adj_matrix:
            result+= ' '.join(map(str,row)) + '\n'
        return result
        
    def display(self):

        print(self)

num_nodes = 5
graph = GraphMatrix(num_nodes)

graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)


graph.display()

print(repr(graph))