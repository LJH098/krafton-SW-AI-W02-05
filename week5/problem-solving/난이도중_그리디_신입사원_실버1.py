# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

"""
TIP: 그리디는 정렬을 해서 푸는 경우가 많다.
정렬의 특성상 한번 확인하면 이전 혹은 이후를 확인할 필요가 없어지는 경우가 많기 때문이다.(문제 축소)
"""

import sys

input = sys.stdin.readline

TEST_CASE = int(input())

for _ in range(TEST_CASE):
    n = int(input())

    arr = [tuple(map(int, input().split())) for _ in range(n)]
    if len(arr) == 1:
        print(1)
        continue

    doc_arr = sorted(arr, key=lambda a: a[0])

    # 서류 1등 먼저 세기
    count = 1
    min_interview = doc_arr[0][1]

    for d, i in doc_arr[1:]:
        if i < min_interview:
            count += 1
            min_interview = i

    print(count)
