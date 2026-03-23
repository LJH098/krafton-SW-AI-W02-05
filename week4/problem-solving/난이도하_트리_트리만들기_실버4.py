# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

from sys import stdin

input = stdin.readline

n, m = map(int, input().split())


cur = 0
for next in range(1, n):
    print(cur, next)
    if cur < n - m:
        cur += 1
