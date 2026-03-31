# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

import sys

input = sys.stdin.readline

TEST_CASE = int(input())
for _ in range(TEST_CASE):
    n = int(input())  # n = 동전 가지수
    arr = list(map(int, input().split()))
    m = int(input())  # m = 만들어야 할 금액
    dp = [0] * (m + 1)
    dp[0] = 1

    for coin in arr:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]
    print(dp[m])
