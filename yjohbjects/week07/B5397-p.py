# B5397 키로거

T = int(input())
for t in range(T):
    log = input()

    stack = []
    temp = []
    for char in log:
        # stack이 비어있고, 화살표나 백스페이스가 나온 경우
        if (char == '-' or char == '<') and len(stack) == 0:
            continue
        # temp가 비어있어서 더이상 우측 화살표가 필요 없는 경우
        elif char == '>' and len(temp) == 0:
            continue

        # 백스페이스
        elif char == '-':
            stack.pop()

        # 화살표
        elif char == '<':
            temp.append(stack.pop())

        elif char == '>':
            stack.append(temp.pop())

        # 알파벳 대문자, 소문자, 숫자
        else:
            stack.append(char)

    while len(temp) != 0:
        stack.append(temp.pop())

    print(''.join(stack))
