# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

from sys import stdin


# list에서 빈칸이 연속해서 2개가 있는지 확인
# 참일 때는 (True, index) 거짓일 때는 (False,0)을 반환
address = stdin.readline().strip()
full_address = []


def fill(word):
    return word.zfill(4)


# ::을 나누면 무조건 두개로 나뉘어짐  (::을 한번만 사용 할 수 있기 때문)
if "::" in address:
    left, right = address.split("::")
    left_group = [fill(g) for g in left.split(":") if g]
    right_group = [fill(g) for g in right.split(":") if g]

    count = 8 - len(left_group) - len(right_group)
    zero_group = ["0000"] * count
    full_address = left_group + zero_group + right_group
else:
    full_address = [fill(g) for g in address.split(":") if g]

print(":".join(full_address))
