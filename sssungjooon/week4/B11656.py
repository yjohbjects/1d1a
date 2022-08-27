# 문자열 S 인풋
S = input()

# 문자열 S의 모든 접미사를 담을 리스트 만들기
word = []

# 문자열은 pop이 안되므로, 글자를 리스트로 한글자씩 쪼개준다.
list_S = list(S)

# S 길이만큼 반복
for i in range(len(list_S)):
    # 그 후 리스트의 글자들을 합치는데
    # 반복할 때마다 앞글자를 pop(0)으로 지워준다.
    word.append(''.join(list_S))
    list_S.pop(0)

# 그 후 sorted로 알파벳순 정렬
new_word = sorted(word)

# 정렬한 것들을 줄별로 출력
for t in new_word :
    print(t)
