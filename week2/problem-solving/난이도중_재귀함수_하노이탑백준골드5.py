# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

from sys import stdin

num = int(stdin.readline())

count = 0


def hanoi(n, start, des, via):
    global count
    if n == 1:
        print(f"{start} {des}")
        count += 1
        return

    # n-1개를 경유지로 옮기기
    hanoi(n - 1, start, via, des)

    # 밑바닥 목적지로 옮기기
    hanoi(1, start, des, via)

    # 경유지로 옮긴 것 목적지로 옮기기
    hanoi(n - 1, via, des, start)


print(2**num - 1)
if num <= 20:
    hanoi(num, 1, 3, 2)
