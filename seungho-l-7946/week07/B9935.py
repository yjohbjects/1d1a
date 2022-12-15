# BAEKJOON 9935 - 문자열 폭발 (G4)

'''
문제
1) 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 됨
2) 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있음
3) 폭발은 폭발 문자열이 문자열에 없을 때까지 계속됨
4) 남아있는 문자가 없는 경우가 있다. 이때는 "FRULA"를 출력함

풀이
1)

입력
1) 첫째 줄에 문자열이 주어짐
2) 둘째 줄에 폭발 문자열이 주어짐

출력
1) 첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력
'''

import sys

sys.stdin = open('B9935.txt')

# input
word = list(sys.stdin.readline().rstrip())
bomb_word = list(sys.stdin.readline().rstrip())
N = len(word)
M = len(bomb_word)
stack = []
result = ''

for i in range(N):
    stack.append(word[i])
    if stack[-1] == bomb_word[-1] and len(stack) >= len(bomb_word):
        for j in range(M):
            if stack[-M + j] != bomb_word[j]:
                break
        else:
            for _ in range(M):
                stack.pop()

# output
if not stack:
    result = 'FRULA'
else:
    result = "".join(stack)
print(result)



# stack = [x for x in bomb_word]
# tmp = []

# while stack:
#     tmp.append(word.pop())
#     if tmp[-1] == stack[-1]:
#         stack.pop()
#         if not stack:
#             for x in bomb_word:
#                 stack.append(x)
#                 tmp.pop()
#             while tmp:
#                 word.append(tmp.pop())
#     else:
#         stack = [x for x in bomb_word]
#         if tmp[-1] == stack[-1]:
#             stack.pop()
#     if not stack and bomb_word in word:
#         stack = [x for x in bomb_word]