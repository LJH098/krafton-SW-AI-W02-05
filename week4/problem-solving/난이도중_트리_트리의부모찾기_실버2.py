# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

import sys

sys.setrecursionlimit(10**6)


def dfs(graph, start, visited, parent):
    visited.add(start)

    for vertex in graph[start]:
        if vertex in visited:
            continue
        else:
            visited.add(vertex)
            parent[vertex] = start
            dfs(graph, vertex, visited, parent)


input = sys.stdin.readline

n = int(input())
visited = set()
parent = [0] * (n + 1)
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited, parent)
for i in range(2, n + 1):
    print(parent[i])
