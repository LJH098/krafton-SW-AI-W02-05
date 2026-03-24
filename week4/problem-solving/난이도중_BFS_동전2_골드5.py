import sys

input = sys.stdin.readline

n, m = map(int, input().split())

coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)


INF = 10**9


dp = [INF] * (m + 1)


dp[0] = 0


for coin in coins:

    for x in range(coin, m + 1):
        # TODO:
        # x - coin원을 만들 수 있었다면
        # dp[x]를 더 작은 값으로 갱신
        if x - coin >= 0:
            dp[x] = min(dp[x], dp[x - coin] + 1)


if dp[m] == INF:
    print(-1)
else:
    print(dp[m])
