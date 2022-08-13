# S12004 구구단

num = int(input())
numbers=list(range(1,10))
 
ans=[]
for a in range(num):
    t_case = int(input())
    for number in numbers:
        answer_rest=t_case % number
        answer_real=t_case // number
        if answer_rest ==0 and answer_real in numbers:
            ans.append('Yes')
            break
    if len(ans)!=a+1:
        ans.append('No')
for b in range(num):
    print(f'#{b+1} {ans[b]}')