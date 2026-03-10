from sys import stdin
import math

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

# 에라토스테네스의 체로 소수 미리 계산
MAX = 10001
sieve = [True] * MAX
sieve[0] = sieve[1] = False

for i in range(2, int(math.sqrt(MAX)) + 1):
    if sieve[i]:
        for j in range(i * i, MAX, i):
            sieve[j] = False

for num in arr:
    for i in range(num // 2, 1, -1):
        if sieve[i] and sieve[num - i]:
            print(f"{i} {num-i}")
            break
