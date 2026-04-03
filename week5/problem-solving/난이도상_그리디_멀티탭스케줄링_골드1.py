# 그리디 - 멀티탭 스케줄링 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1700

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
INF = 10**6
arr = list(map(int, input().split()))

select = set([arr[0]])
count = 0
for item in range(1, k):
    if arr[item] in select:
        continue

    if len(select) < n:
        select.add(arr[item])

    else:
        target = None
        farthest = -1

        for s in select:
            found = False
            
            for i in range(item + 1, k):
                if arr[i] == s:
                    found = True
                    if i > farthest:
                        farthest = i
                        target = s
                    break

            if not found:
                target = s
                break

        select.remove(target)
        count += 1
        select.add(arr[item])

print(count)
