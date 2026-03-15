# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
from sys import stdin

readline = stdin.readline
n = int(readline())
num_list = list(map(int, readline().split()))
dic = {}
for i in range(n):
    dic[num_list[i]] = 0

n2 = int(readline())
num2_list = list(map(int, readline().split()))
for i in range(n2):
    if num2_list[i] in dic.keys():
        print("1")
    else:
        print("0")
