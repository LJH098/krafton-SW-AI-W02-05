# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

from sys import stdin

readline = stdin.readline

stack = []


def push(x):
    stack.append(x)


def pop():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack.pop())


def size():
    print(len(stack))


def empty():
    size = len(stack)
    print(1 if size == 0 else 0)


def top():
    if len(stack) == 0:
        print("-1")
    else:
        print(stack[len(stack) - 1])


n = int(readline())

for i in range(n):
    command_list = readline().split()
    if len(command_list) > 1:
        push(command_list[1])
    else:
        command = command_list[0]
        match command:
            case "pop":
                pop()
            case "size":
                size()
            case "empty":
                empty()
            case "top":
                top()
