import sys
sys.stdin = open('in.txt')

N = int(input())
M = int(input())
S = input()
i = 0
cnt = 0
result = 0
while i + 2 < M:
    if S[i] == 'I' and S[i + 1] == 'O' and S[i + 2] == 'I':
        cnt += 1
        if cnt == N:
            result += 1
            cnt -= 1

        i += 2
    else:
        cnt = 0
        i += 1

print(result)