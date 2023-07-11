N = int(input())

star = '*'
void = ' '

for i in range(1, 2 * N):
    if i > N:
        print(star * (2 * N - i ))
    else:
        print(star * i)
