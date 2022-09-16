from itertools import permutations
'''
파이썬으로 제출하면 런타임 에러뜨고 
pypy3로 제출하면 통과되는 코드..!
'''

def calculate(cals):
    n1 = nums[0]
    for idx, cal in enumerate(cals):
        n2 = nums[idx+1]
        if cal == '+':
            n1 = n1+n2
        elif cal == '-':
            n1 = n1-n2
        elif cal == '*':
            n1 = n1*n2
        elif cal == '/':
            if n1 < 0:
                n1 = -n1
                n1 = n1//n2
                n1 = -n1
            else:
                n1 = n1//n2
    return n1


N = int(input())
nums = list(map(int, input().split()))
cals = list(map(int, input().split()))
cal = ''
answers = []
for idx, cnt in enumerate(cals):
    if idx == 0:
        for _ in range(cnt):
            cal += '+'
    elif idx == 1:
        for _ in range(cnt):
            cal += '-'
    elif idx == 2:
        for _ in range(cnt):
            cal += '*'
    elif idx == 3:
        for _ in range(cnt):
            cal += '/'
perms = list(permutations(cal, len(cal)))
for perm in perms:
    answers.append(calculate(perm))
answers = sorted(answers)
print(answers[-1])
print(answers[0])
