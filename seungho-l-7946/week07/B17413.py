# BAEKJOON 17413 - 단어 뒤집기 2 (S3)

'''
문제
1) <>로 이루어진 것을 태그라고 부르며, 공백으로 분류되는 나머지는 단어임.
2) 태그는 뒤짚지 않고, 단어만 각각 뒤집어서 출력하는 프로그램을 만들것.

풀이
1) 공백과 <> 를 잘 구분하여 조건문을 만듦

입력
1) 첫째 줄에 문자열 S가 주어짐.

출력
1) 첫째 줄에 문자열 S의 단어를 뒤집어서 출력함.
'''

import sys

sys.stdin = open('B17413.txt')

# input
sentence = input()
result = ''
tmp = []

for text in sentence:
    if text == '<':
        while tmp:
            result += tmp.pop()
        tmp = []
        result += text
        continue
    if result and result[-1] == '<':
        if text == '>':
            tmp.append(text)
            result += "".join(tmp)
            tmp = []
        else:
            tmp.append(text)
    else:
        if text == ' ':
            while tmp:
                result += tmp.pop()
            result += ' '
        else:
            tmp.append(text)
while tmp:
    result += tmp.pop()

# output
print(result)