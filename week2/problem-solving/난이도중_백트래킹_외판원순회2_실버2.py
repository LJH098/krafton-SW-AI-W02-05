# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
from sys import stdin

n = int(stdin.readline())
w = [list(map(int, stdin.readline().split())) for _ in range(n)]

lowest = float("inf")


def tsp(start, current, visited, cost):
    global lowest

    if cost >= lowest:
        return

    if len(visited) == n:
        if w[current][start] != 0:
            lowest = min(lowest, cost + w[current][start])
            return

    for next_city in range(n):
        if next_city not in visited and w[current][next_city] != 0:
            visited.append(next_city)
            tsp(start, next_city, visited, cost + w[current][next_city])
            visited.pop()


tsp(0, 0, [0], 0)
print(lowest)
