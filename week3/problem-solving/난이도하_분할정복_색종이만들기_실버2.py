# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
# 이 문제를 dc를 완전탐색으로 풀어냈지만 누적합 방법이 더 빠르다...
from sys import stdin

readline = stdin.readline

white_count = 0
blue_count = 0


# i: 가로 시작 인덱스, i : 세로 시작 배열 , k: 한변의 길이
def dc(i, j, k):
    global white_count
    global blue_count
    if k == 0:
        return

    memory = None

    for m in range(i, k + i):
        for n in range(j, k + j):

            if m == i and n == j:
                memory = arr[m][n]
            else:
                if arr[m][n] != memory:
                    half = k // 2
                    dc(i, j, half)  # 왼쪽 위
                    dc(i, j + half, half)  # 오른쪽 위
                    dc(i + half, j, half)  # 왼쪽 아래
                    dc(i + half, j + half, half)  # 오른쪽 아래
                    return
    if memory == 1:
        blue_count += 1
    else:
        white_count += 1


n = int(readline())
arr = [list(map(int, input().split())) for _ in range(n)]
dc(0, 0, n)
print(white_count)
print(blue_count)
