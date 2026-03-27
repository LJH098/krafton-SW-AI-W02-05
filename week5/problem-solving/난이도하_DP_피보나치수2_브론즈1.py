# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

from sys import stdin

input = stdin.readline

n = int(input())
memory = {}


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    if n in memory:
        return memory[n]

    memory[n] = fib(n - 1) + fib(n - 2)
    return memory[n]


print(fib(n))
