class Graph:
    def __init__(self):
        self.graph={}

    def add_edge(self, u, v):#aading an undriected edge between two nodes, u and v
        #if u and v are not in the graph, we add/initialise it with an empty list
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)#adding node v as a neighbour to node u and vice versa, making the edge directed
        self.graph[v].append(u)

    def dfs_iterative(self,starting_node):
        stack = [starting_node]# A stack is used to keep track of the nodes
        visited = set()#an empty set is used to keep trrack of visited nodes

        result = []# this is used to keep a track of the visited nodes

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                result.append(current)

                for neighbour in reversed(self.graph[current]):#we use reversed here since the stack is a LIFO structure to ensure that the traversal follows the correct order.
                    if neighbour not in visited:
                        stack.append(neighbour)

        return result
