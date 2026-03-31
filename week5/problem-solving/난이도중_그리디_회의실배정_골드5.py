# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys

input = sys.stdin.readline

n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
if len(arr) == 1:
    print(1)
    sys.exit()

arr.sort(key=lambda a: (a[1], a[0]))

select = arr[0]
count = 1

for a, b in arr[1:]:
    if a >= select[1]:
        count += 1
        select = (a, b)
print(count)
