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

def bfs(graph, source):
    visited = [False] * len(graph.data)
    queue = []
    
    visited[source] = True    
    queue.append(source)
    
    traversal_order = []  
    
    while queue:
        current = queue.pop(0)  
        
        traversal_order.append(current)  
        
        
        for neighbor in graph.data[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return traversal_order

g1 = Graph()


g1.add_edge(0, 1)
g1.add_edge(0, 4)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(1, 4)
g1.add_edge(2, 3)
g1.add_edge(3, 4)
print(bfs(g1, 3))