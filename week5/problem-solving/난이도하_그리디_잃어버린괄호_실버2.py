# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

import sys

input = sys.stdin.readline
total = 0
arr = input().split("-")
for i in range(len(arr)):
    if i == 0:
        if "+" in arr[i]:
            total += sum(int(num) for num in arr[i].split("+"))
        else:
            total += int(arr[i])
    else:
        if "+" in arr[i]:
            total -= sum(int(num) for num in arr[i].split("+"))
        else:
            total -= int(arr[i])
print(total)
