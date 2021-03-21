from collections import defaultdict, deque
from typing import Dict, List

graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [3, 4]

queue = deque()
visited = []
goal = 3

def bfs(G: Dict[int, List[int]], root: int):
    visited.append(root)
    queue.append(root)
    while queue:
        v = queue.pop()
        if v == goal:
            return v
        for w in G[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return "Not found"

print(bfs(graph, 0))
