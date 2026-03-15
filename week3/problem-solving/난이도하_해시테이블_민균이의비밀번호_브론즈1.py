# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
from sys import stdin

n = int(stdin.readline())
pwd = {}

for i in range(n):
    pwd[stdin.readline().strip()] = 0


for word in pwd.keys():
    reversed_word = word[::-1]
    if reversed_word in pwd:
        length = len(word)
        half = (length - 1) // 2
        print(f"{length} {word[half]}")
        break
