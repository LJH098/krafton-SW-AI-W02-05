# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

# 최소 칸 -> bfs
from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

queue = deque([(0, 0)])
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
dist = [[0] * m for _ in range(n)]
dist[0][0] = 1
while queue:
    r, c = queue.popleft()
    if r == n - 1 and c == m - 1:
        print(dist[r][c])
        break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and arr[nr][nc] == 1:
            visited[nr][nc] = True
            dist[nr][nc] = dist[r][c] + 1
            queue.append((nr, nc))
