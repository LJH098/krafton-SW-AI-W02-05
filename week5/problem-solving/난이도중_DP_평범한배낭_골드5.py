# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys

input = sys.stdin.readline

# n은 물품 수  , k는 총 무게
# 주의해야 할 점 : 물건의 종류당 여러개를 담을 수 있는게 아니라 1개씩만 담을 수 있다.
n, k = map(int, input().split())

arr = [tuple(map(int, input().split())) for i in range(n)]


dp = [0] * (k + 1)

for w, v in arr:
    for i in range(k, w - 1, -1):
        dp[i] = max(dp[i - w] + v, dp[i])
print(dp[k])
