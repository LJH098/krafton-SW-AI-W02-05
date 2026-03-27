# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

count = 0
for i in range(len(arr) - 1, -1, -1):
    if arr[i] > m:
        continue
    n = m // arr[i]
    m %= arr[i]
    count += n
print(count)
