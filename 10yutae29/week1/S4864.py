# S4864 문자열 비교

num = int(input())
answers=[]
for test_case in range(num):
    str1 = input()
    str2 = input()
    if str1 in str2:
        answers.append(1)
    else:
        answers.append(0)
for ans_num in range(len(answers)):
    print(f'#{ans_num+1} {answers[ans_num]}')