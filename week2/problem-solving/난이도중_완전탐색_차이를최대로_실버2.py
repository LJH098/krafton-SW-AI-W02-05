# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819
from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
maximum = 0


def backtrack(current, total, remember):
    global maximum

    if len(remember) == n:
        maximum = max(maximum, total)
        return

    for num in range(n):
        if num not in remember:
            remember.add(num)
            backtrack(
                num,
                total + abs(arr[current] - arr[num]),
                remember,
            )
            remember.remove(num)


for i in range(n):
    backtrack(i, 0, {i})
print(maximum)
