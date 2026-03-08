# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478
def listen_to_me(k):
    if k == n:
        what_is_recursive(k)
        return
    word1 = '"재귀함수가 뭔가요?"'
    word2 = (
        '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
    )
    word3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
    word4 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'

    line = "____" * k
    print(line + word1)
    print(line + word2)
    print(line + word3)
    print(line + word4)

    listen_to_me(k + 1)


def what_is_recursive(k):
    line = "____" * k
    word1 = '"재귀함수가 뭔가요?"'
    word2 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
    print(line + word1)
    print(line + word2)
    do_answer(k)


def do_answer(k):
    if k < 0:
        return
    line = "____" * k
    word1 = "라고 답변하였지."
    print(line + word1)
    do_answer(k - 1)


n = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
listen_to_me(0)
