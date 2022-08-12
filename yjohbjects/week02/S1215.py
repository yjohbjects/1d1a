import sys
sys.stdin = open('S1215_input.txt')

# S1215 회문 1

for z in range(10):

    N = int(input())
    words = [list(map(str, input())) for _ in range(8)]

    temp = ''
    cnt = 0

    # 가로맨
    for i in range(8):
        for j in range(8-N+1):
            # print(words[i][j])
            temp = words[i][j:j+N]
            if temp == temp[::-1]:
                cnt += 1

    # 세로맨
    for j in range(8):
        for i in range(8-N+1):
            temp = []
            for x in range(N):
                temp += words[i+x][j]
            if temp == temp[::-1]:
                cnt += 1

    print(f'#{z+1} {cnt}')