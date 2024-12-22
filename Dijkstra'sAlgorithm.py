class Graph:
    def __init__(self):
        self.graph = {} 

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start, target):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0  
        visited = set() 
        unvisited_nodes = list(self.graph.keys())  

        while unvisited_nodes:
            current_node = min(
                (node for node in unvisited_nodes if node not in visited),
                key=lambda node: distances[node],
                default=None)
            
            if current_node is None or current_node == target:
                break

            visited.add(current_node)  
            unvisited_nodes.remove(current_node)

            for neighbor, weight in self.graph.get(current_node, []):
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
        return distances.get(target, "Unreachable") if distances.get(target) != float('inf') else "Unreachable"


# Create a graph
g = Graph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 2)
g.add_edge(1, 3, 10)
g.add_edge(2, 1, 5)
g.add_edge(2, 3, 3)
g.add_edge(3, 4, 4)
g.add_edge(3, 5, 11)
source = 0
target = 5

# Find the shortest path from source to target
shortest_distance = g.dijkstra(source, target)
print(f"The shortest distance from node {source} to node {target} is {shortest_distance}")
