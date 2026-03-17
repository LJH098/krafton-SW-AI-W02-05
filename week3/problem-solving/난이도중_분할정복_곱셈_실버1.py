# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629


from sys import stdin

readline = stdin.readline

arr = list(map(int, readline().split()))
a, b, c = arr[0], arr[1], arr[2]


def dc(k):
    if k == 1:
        return a % c

    half = dc(k // 2)

    if k % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c


print(dc(b))
