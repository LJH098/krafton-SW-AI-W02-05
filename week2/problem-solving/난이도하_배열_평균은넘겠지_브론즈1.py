# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

from sys import stdin

TEST_CASE = int(stdin.readline())

for i in range(TEST_CASE):
    student_info = list(map(int, stdin.readline().split()))
    sum = 0
    over = 0
    sl = len(student_info)
    for j in range(1, sl):
        sum += student_info[j]
    avg = sum / (sl - 1)

    for j in range(1, sl):
        if student_info[j] > avg:
            over += 1

    ratio = (over / (sl - 1)) * 100
    format_ratio = round(ratio, 3)
    print(f"{format_ratio}%")
