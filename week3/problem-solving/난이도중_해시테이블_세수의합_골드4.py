# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295

# a+b+c = k -> a+b = k-c
# k가 최대
from sys import stdin

readline = stdin.readline

n = int(readline())
arr = list(int(readline()) for _ in range(n))
sum_set = set()

arr.sort(reverse=True)

# a+b에서 최대값은 제외하고 생각한다
# a+b 에서 a와 b중 최대값이 포함되면 이미 최대값음 넘어버림
for i in range(1, len(arr)):
    for j in range(i, len(arr)):
        sum_set.add(arr[i] + arr[j])


# k와 c는 같을 수 없다 -> a+b이 0이 될 수 없기 때문
# for문에서 arr[i] - arr[j] in sum_set 조건이 만족하면 바로 빠져나온다.
# 그래야 i가 가장 작고 i가 작다는 것은 k가 크다는 것
boolean = False
for i in range(len(arr)):
    if boolean:
        break
    for j in range(i + 1, len(arr)):
        if arr[i] - arr[j] in sum_set:
            print(arr[i])
            boolean = True
            break
