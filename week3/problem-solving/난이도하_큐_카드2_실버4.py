# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from sys import stdin
from collections import deque

card_queue = deque()
drop_queue = []
n = int(stdin.readline())

# 4,3,2,1 -> 4,3,2 drop = 1 -> 2,4,3 drop =1
for i in range(1, n + 1):
    card_queue.append(i)

while len(card_queue) > 1:
    card_queue.popleft()  # 버리기
    card = card_queue.popleft()
    card_queue.append(card)

print(card_queue[0])
