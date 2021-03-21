from collections import defaultdict
from typing import Dict, List

graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [3, 4]

visited = []
def dfs(G: Dict[int, List[int]], v: int):
    visited.append(v)
    for w in G[v]:
        if w not in visited:
            dfs(G, w)

print(visited)
dfs(graph, 0)
print(visited)
