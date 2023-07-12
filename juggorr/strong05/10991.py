N = int(input())

star = '*'
void_star = ' *'
void = ' '

for i in range(N):
    print(void * (N - i - 1) + star + void_star * i)
    