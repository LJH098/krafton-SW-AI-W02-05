# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

from sys import stdin
from collections import deque

input = stdin.readline

TEST_CASE = int(input())
# n = 국가의 수, m = 비행기 종류
for _ in range(TEST_CASE):
    n, m = map(int, input().split())

    graph = {i: [] for i in range(1, n + 1)}
    visited = set([1])
    queue = deque([1])
    count = 0

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    while len(visited) < n:
        vertex = queue.popleft()
        for v in graph[vertex]:
            if v in visited:
                continue
            else:
                visited.add(v)
                queue.append(v)
                count += 1
    print(count)
