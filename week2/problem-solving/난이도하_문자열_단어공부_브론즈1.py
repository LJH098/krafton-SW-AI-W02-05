# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
import sys
from sys import stdin

words = list(input().lower())
set_words = list(set(words))
alpha = {}

if len(set_words) == 1:
    print(set_words[0].upper())
    sys.exit(0)

for sw in set_words:
    alpha[sw] = words.count(sw)

max_word = max(alpha, key=lambda x: alpha[x])

duplicate = False
for key, value in alpha.items():
    if key != max_word and value == alpha[max_word]:
        duplicate = True
        break
if duplicate:
    print("?")
else:
    print(max_word.upper())
