# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606


import sys

input = sys.stdin.readline


def dfs(graph, start, visited):
    global count
    visited.add(start)

    for vertex in graph[start]:
        if vertex in visited:
            continue
        else:
            visited.add(vertex)
            dfs(graph, vertex, visited)
    return visited


n = int(input())
m = int(input())

if m == 0:
    print(0)
    sys.exit()

visited = set()
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited)
print(len(visited) - 1)
