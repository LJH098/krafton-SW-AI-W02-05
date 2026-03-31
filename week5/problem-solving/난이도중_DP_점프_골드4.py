# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253

# 1번돌에서 무조건 1칸만 점프 할 수 있고
# 그 다음번에는 이전칸에 x칸 점프해싿면 x-1, x, x+1 칸 점프 가능
# 단 무조건 앞으로만 가니까 x-1이 음수면 고려안함
# 몇 개의 돌은 크기가 너무 작기 때문에 여기로는 점프 못함


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
blocked = set(int(input()) for _ in range(m))

if n == 1:
    print(0)
    sys.exit()

INF = 10**9
max_jump = int((2 * n) ** 0.5) + 2

dp = [[INF] * (max_jump + 1) for _ in range(n + 1)]

if 2 not in blocked:
    dp[2][1] = 1

for stone in range(2, n + 1):
    if stone in blocked:
        continue

    for jump in range(1, max_jump + 1):
        if dp[stone][jump] == INF:
            continue

        for next_jump in (jump - 1, jump, jump + 1):
            if next_jump <= 0:
                continue

            next_stone = stone + next_jump

            if next_stone > n or next_stone in blocked:
                continue

            dp[next_stone][next_jump] = min(
                dp[next_stone][next_jump], dp[stone][jump] + 1
            )

answer = min(dp[n])
print(-1 if answer == INF else answer)
