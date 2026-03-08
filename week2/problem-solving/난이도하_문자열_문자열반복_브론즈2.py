# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

from sys import stdin

TEST_CASE = int(stdin.readline())

for i in range(TEST_CASE):
    k, m = stdin.readline().split()
    list_m = list(m)
    n = int(k)
    answer = ""

    for j in range(len(list_m)):
        word = list_m[j] * n

        answer += word
    print(answer)
