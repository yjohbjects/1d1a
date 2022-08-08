# S4835 구간합

T = int(input())
answers = []

for num in range(T):
    test_case = list(map(int,input().split()))
    N = test_case[0]
    M = test_case[1]
    test_list = list(map(int,input().split()))
    ans_list = []
    for a in range(N-M+1):
        ans = sum(list(test_list[a:a+M]))
        ans_list.append(ans)
    answers.append(max(ans_list)-min(ans_list))
for b in range(len(answers)):
    print(f'#{b+1} {answers[b]}')