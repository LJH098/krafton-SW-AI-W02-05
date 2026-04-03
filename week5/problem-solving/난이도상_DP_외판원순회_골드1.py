import sys

input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

INF = 10**9

# dp[cur][visited]
# 의미:
# 현재 cur 도시에 있고,
# visited 상태의 도시들을 이미 방문했을 때,
# 남은 도시를 모두 방문하고 0번 도시로 돌아가는 최소 비용
dp = [[-1] * (1 << n) for _ in range(n)]


def dfs(cur, visited):
    # 1. 모든 도시를 방문한 경우
    #    현재 cur 에서 0으로 돌아갈 수 있으면 그 비용 반환
    #    없으면 INF 반환
    if visited == (1 << n) - 1:
        # TODO:
        if w[cur][0] == 0:
            return INF
        return w[cur][0]

    # 2. 이미 계산한 상태면 바로 반환
    # 메모이제이션

    if dp[cur][visited] != -1:
        return dp[cur][visited]

    # 3. 일단 현재 상태의 최소 비용을 INF로 시작

    dp[cur][visited] = INF

    # 4. 다음 도시 후보들을 전부 확인
    for nxt in range(n):
        # TODO 1: 이미 방문한 도시면 continue
        # TODO 2: cur -> nxt 로 갈 수 없으면 continue
        # TODO 3:
        # next_visited = visited | (1 << nxt)
        # cost = w[cur][nxt] + dfs(nxt, next_visited)
        # dp[cur][visited] = min(dp[cur][visited], cost)
        pass

    # 5. 계산 결과 반환
    # TODO:
    # return dp[cur][visited]
    pass


# 시작은 0번 도시에서 시작, 0번만 방문한 상태
answer = dfs(0, 1 << 0)
print(answer)
