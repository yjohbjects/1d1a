import sys
sys.stdin = open('input_B11656.txt')
# 우선 단어를 단어 하나하나 쪼개서 리스트로 받는다
word = list(map(str, input()))
# 단어의 접미사들이 들어갈 빈 리스트를 만들어준다
word_lst = [0] * len(word)
# 단어의 길이만큼 반복을 돌면서
for i in range(len(word)):
    # 단어 리스트의 i번째 원소는 단어를 앞에서 i번째부터 슬라이싱한 리스트를 넣어준다
    word_lst[i] = word[i:]
    # 그리고 그 리스트를 단어로 뭉쳐준다
    word_lst[i] = ''.join(word_lst[i])
# 단어 리스트를 단어 순으로 정렬
word_lst = sorted(word_lst)
for sorted_word in word_lst:
    print(sorted_word)
