S = list(map(str,input()))

# 구분 짓는 <, >, 빈칸
devide = ['<','>',' ']

# 단어들을 넣어서 합쳐서 내보낼 stack 리스트
word_make = []

New_S = []

# New_S => 구분자에 따라 단어를 구분지어서 묶어주는 과정
for word in S :
    # S의 문자열 중 구분 짓는 3가지 중 없다면 스택에 넣기
    if word not in devide :
        word_make.append(word)

        # 그 word가 문자열의 마지막 단어인 경우
        # if word == S[-1] :
        #     New_S.append(''.join(word_make)) = > 이렇게 하면 문자열의 마지막과 같은 단어가 나오면 다 끊긴다.

    # S의 문자열이 구분 짓는 3가지에 있다면 들어간 단어들 합쳐서 
    elif word in devide :
        # word_make stack에 들어가있는게 없다면 그대로 New_S로 직행
        if not word_make :
            New_S.append(word)
        # word_make stack에 들어가있는게 있다면 있는 단어 합치고, 구분자도 넣기
        # 그 후 스택 초기화
        else :
            # New_S.append((''.join(word_make))[::-1])
            New_S.append(''.join(word_make))
            word_make = []
            New_S.append(word)
# 혹시나 남아있는 문자열이 있다면 합쳐서 New_S에 넣어준다.
if word_make :
    # New_S.append((''.join(word_make))[::-1])
    New_S.append(''.join(word_make))

# 추가 조건이 있었다!!!!
# < >의 경우 안에 있는 글자들을 뒤집지 않는다.
plus_stack = []

New_New_S = []

# New_New_S => 구분지어서 묶은 단어들을 < > 유무에 따라 뒤집어서 넣어주는 과정

# 괄호가 있는 < > 경우와 없는 경우로 나눠준다.
# 먼저 < > 가 있는 경우 (예시에는 < 하나만 있어도 양쪽 쌍이 다 있다.)
if '<' in New_S :
    for new_word in New_S :
        if new_word == '<' :
            # 여는 괄호인데 2번째 스택에 단어가 있다면 일단 합쳐준다. 뒤집어서 New_New_S에 넣는다.
            if plus_stack :
                # New_New_S.append((''.join(plus_stack))[::-1])
                # plus_stack의 개별 요소들을 하나씩 뒤집어서 넣는다.
                temp = []
                for p in plus_stack :
                    temp.append(p[::-1])
                New_New_S.append((''.join(temp)))
                plus_stack = []
                plus_stack.append(new_word)
            elif not plus_stack :
                plus_stack.append(new_word)
        # 닫는 괄호 나오면 닫는 괄호까지 넣은 후 2번째 스택에 있는 단어를 2차 분류 리스트에 넣는다.
        elif new_word == '>' :
            plus_stack.append(new_word)
            New_New_S.append(''.join(plus_stack))
            # 그후 스택 비우기
            plus_stack = []
        else :
            plus_stack.append(new_word)
    # 이 과정에서도 마찬가지로 남아있는 문자열이 있다면 뒤집어서 New_New_S에 넣어준다.
    if plus_stack :
        temp = []
        for p in plus_stack :
            temp.append(p[::-1])
        New_New_S.append((''.join(temp)))
# < > 없는 경우, 하나씩 뒤집어서 넣어준다.
else :
    for new_word in New_S :
        New_New_S.append(new_word[::-1])

# 모든 재탄생 과정을 거쳤으면 글자들을 합쳐준다.
result = ''.join(New_New_S)
# print(New_S)
# print(New_New_S)
print(result)

# 1차 실험결과 3,5, 6 틀림
# 2차 통과
