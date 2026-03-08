# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

from sys import stdin

list = []
for i in range(9):
    n = int(stdin.readline())
    list.append(n)

max = 0
line = 0
for i in range(9):
    if i == 0:
        max = list[0]
        line = 1
    elif list[i] > max:
        max = list[i]
        line = i + 1

print(max)
print(line)
