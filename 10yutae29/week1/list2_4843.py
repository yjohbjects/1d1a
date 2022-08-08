# S4843 특별한 정렬

num=int(input())
answers=[]
for test_case in range(num):
    numbers = int(input())
    cases = list(map(int,input().split()))
    lower_case = sorted(cases)
    upper_case = sorted(cases,reverse=True)
    lower_ans = lower_case[0:numbers//2]
    upper_ans = upper_case[0:numbers//2]        
    for i in range(len(upper_ans)):
        upper_ans.insert(2*i+1,lower_ans[i])
    answers.append(upper_ans)

for ans_num in range(len(answers)):
    answer = list(map(str,answers[ans_num][:10]))
    answer = ' '.join(answer)
    print(f'#{ans_num+1} {answer}')