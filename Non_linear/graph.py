class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

print("BFS:")
g.bfs('A')

print("\nDFS:")
g.dfs('A')