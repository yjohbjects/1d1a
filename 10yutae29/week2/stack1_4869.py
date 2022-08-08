# S4869 종이붙이기

T = int(input())

for t in range(T):
    N = int(input())//10
    if N%2 ==1:
        ans=0
        for n in range(1,N+1):
            if n%2 ==1:
                ans += 2**(n-1)
        print(f'#{t+1} {ans}')
    else:
        ans=0
        for n in range(1,N+1):
            if n ==2:
                ans += 3

            elif n%2 == 0:
                ans += 2**(n-1)
        print(f'#{t+1} {ans}')