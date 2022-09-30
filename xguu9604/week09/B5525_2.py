import sys
sys.stdin = open('input_B5525.txt')

N = int(input())
M = int(input())
ioi = input()
answer, i, num_ioi = 0, 0, 0

while i < (M - 1):
    if ioi[i:i+3] == 'IOI':
        i += 2
        num_ioi += 1
        if num_ioi == N:
            answer += 1
            num_ioi -= 1
    else:
        i += 1
        num_ioi = 0

print(answer)
