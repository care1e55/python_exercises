# DFS travfersal
# BFS travfersal (optional)
# Make it OOP style

# n - number of nodes
# then n inputs is nodes in format v1 v2
from collections import defaultdict
from typing import List, Dict, Optional


def read_input() -> Dict:
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        v1, v2 = tuple(int(v) for v in input().split())
        graph[v1].append(v2)
    return graph


def dfs(start, graph: Dict) -> None:
    vertices = graph.get(start)
    if vertices:
        for v in vertices:
            print(v)
            dfs(v, graph)
    return


class Vertex:
    def __init__(self, number):
        self.number = number
        self._children: List[Vertex] = []

    @property
    def children(self):
        return self._children

    def add_child(self, child):
        self._children.append(child)

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)


class Tree:
    def __init__(self, v: Vertex):
        self.root = v

    def _find_vertex(self, v, verbose) -> Optional[Vertex]:
        return self.traverse(self.root, v, verbose)

    def add_node(self, v1, v2, verbose=False):
        vertex = self._find_vertex(v1, verbose)
        print(vertex)
        if vertex:
            if verbose:
                print(f"Adding {v2} to {vertex}")
            vertex.add_child(v2)

    def traverse(self, start: Vertex, end: Vertex = None, verbose=False, ) -> Optional[Vertex]:
        vertex = None
        if verbose:
            print(start)
        if end is not None and end.number == start.number:
            return start
        if start.children:
            for v in start.children:
                vertex = self.traverse(v, end, verbose)
                if vertex:
                    return vertex
        return vertex

    def __str__(self):
        pass


if __name__ == '__main__':
    graph = read_input()
