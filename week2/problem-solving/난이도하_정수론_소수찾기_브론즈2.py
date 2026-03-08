# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

from sys import stdin
import math


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    sqrt = math.trunc(math.sqrt(num))

    for i in range(3, sqrt + 1, 2):
        if num % i == 0:
            return False
    return True


n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

answers = [i for i in nums if is_prime(i)]
print(len(answers))
