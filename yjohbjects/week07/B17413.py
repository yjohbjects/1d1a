# B17413 단어 뒤집기2

"""
is_sign 불리안을 지정해서,
True일 때는 result +=
    * 단 True일 때는 stack이 비어있어야한다
False일 떄는 stack에 저장
"""

word = input()
result = ''
stack = []
is_sign = False

for char in word:
    if char == '<':
        is_sign = True
    elif char == '>':
        is_sign = False
        result += char
        continue

    if is_sign == True and stack:
        while stack:
            result += stack.pop()
        result += char

    elif is_sign == True and len(stack) == 0:
        result += char

    elif is_sign == False and char == ' ':
        while stack:
            result += stack.pop()
        result += char

    else: # False
        stack.append(char)

if stack:
    while stack:
        result += stack.pop()

print(result)