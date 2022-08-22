# S5097 회전

T = int(input())

for t in range(T):
    nm = list(map(int,input().split()))
    number = nm[0]
    repeat = nm[1]
    num_list = list(map(int, input().split()))
    print(f'#{t+1} {num_list[repeat % number]}')
