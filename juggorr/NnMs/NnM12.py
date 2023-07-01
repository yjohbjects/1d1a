import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

answer = [0] * M
pre_num = -1

def NnM12(cnt, idx, cur_num):
    global pre_num

    if cur_num == pre_num:
        return
    
    else:
        pre_num = -1

        if cnt == M:
            print(*answer)
            return
        
        for i in range(idx, N):
            answer[cnt] = numbers[i]
            NnM12(cnt + 1, i, numbers[i])
            answer[cnt] = 0
            pre_num = numbers[i]

NnM12(0, 0, 0)