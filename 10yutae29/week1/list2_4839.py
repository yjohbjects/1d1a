# S4839 이진탐색

num = int(input())
answers=[]
for n in range(num):
    test_case= list(map(int,input().split()))
    P = test_case[0]
    Pa = test_case[1]
    Pb = test_case[2]
    a_l=1
    b_l=1
    a_count = 0
    b_count = 0
    a_r = P
    b_r = P
    a_condition = 0
    b_condition = 0
    while True:
        a_c = int((a_l+a_r)/2)
        b_c = int((b_l+b_r)/2)
        
        if a_condition == 0:
            if a_c == Pa:
                a_count += 1
                a_condition = 1
            elif a_c < Pa:
                a_l = a_c
                a_count += 1
            elif a_c > Pa:
                a_r = a_c
                a_count += 1
        if b_condition == 0:
            if b_c == Pb:
                b_count += 1
                b_condition = 1
            elif b_c < Pb:
                b_l = b_c
                b_count += 1
            elif b_c > Pb:
                b_r = b_c
                b_count += 1
        if a_condition == 1 and b_condition == 1:
            if a_count == b_count:
                answers.append('0')
                
            elif a_count > b_count:
                answers.append('B')
                
            else:
                answers.append('A')
            break
for an_num in range(len(answers)):
    print(f'#{an_num+1} {answers[an_num]}')