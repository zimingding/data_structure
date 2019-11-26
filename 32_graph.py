from collections import deque


class Graph:
    def __init__(self, v: int):
        self.data = [[] for _ in range(v)]
        self.v = v
        self.visited = [False] * v
        self.found = False

    def addEdge(self, s: int, t: int):
        self.data[s].append(t)
        self.data[t].append(s)

    def search(self, s: int, t: int) -> bool:
        self.dfs(s, t)
        return self.found

    def dfs(self, s: int, t: int):
        if self.found:
            return

        if s == t:
            self.found = True
            return

        self.visited[s] = True
        nodes = self.data[s]
        for node in nodes:
            if not self.visited[node]:
                self.dfs(node, t)

    def bfs(self, s: int, t: int) -> bool:
        q = deque([s])
        while q:
            node = q.popleft()
            if not self.visited[node]:
                if node == t:
                    return True
                self.visited[node] = True
                for x in self.data[node]:
                    q.append(x)
        return False


graph = Graph(8)
graph.addEdge(0, 1)
graph.addEdge(0, 3)
graph.addEdge(1, 2)
graph.addEdge(1, 4)
graph.addEdge(2, 5)
graph.addEdge(3, 4)
graph.addEdge(4, 5)
graph.addEdge(4, 6)
graph.addEdge(5, 7)
graph.addEdge(6, 7)

print(graph.bfs(0, 7))
