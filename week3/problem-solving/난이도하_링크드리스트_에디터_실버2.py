# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406


from sys import stdin

arr = list(stdin.readline().strip())
n = int(stdin.readline())

# arr = [a,b,c].  stack = [0,1,2,3]
# abcd
left_stack = arr
right_stack = []

for i in range(n):
    w = stdin.readline().strip()
    if w == "L":
        if len(left_stack) == 0:
            continue
        data = left_stack.pop()
        right_stack.append(data)
    elif w == "D":
        if len(right_stack) == 0:
            continue
        data = right_stack.pop()
        left_stack.append(data)
    elif w == "B":
        if len(left_stack) == 0:
            continue
        left_stack.pop()
    else:
        data = w.split(" ")[1]
        left_stack.append(data)

for i in range(len(right_stack) - 1, -1, -1):
    left_stack.append(right_stack[i])
print("".join(left_stack))
