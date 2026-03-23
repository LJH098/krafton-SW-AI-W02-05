# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())

graph = {i: set() for i in range(n * n)}

queue = deque([0])

visited = set([0])
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break

        vertex = (i * n) + j
        right = vertex + arr[j]
        down = vertex + n * arr[j]

        if right < (i * n) + n:
            graph[vertex].add(right)

        if down <= (n - 1) * n + j:
            graph[vertex].add(down)

result = False
boolean = False
while queue:
    if boolean:
        break
    vertex = queue.popleft()
    for v in graph[vertex]:
        if v == n * n - 1:
            boolean = True
            result = True
            break
        if v in visited:
            continue
        else:
            queue.append(v)
            visited.add(v)


print("HaruHaru") if result else print("Hing")
