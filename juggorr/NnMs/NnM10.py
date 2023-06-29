import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

checked = [0] * (N + 1)
answer = [0] * M
pre_num = -1

def NnM10(cnt, idx, cur_num):
    global pre_num

    # 현재 들어오는 숫자가 이전에 빠진 숫자와 같다면 그대로 종료
    if cur_num == pre_num:
        return
    
    # 다르다면
    else:
        # 전에 빠진 숫자를 초기화 해주고
        pre_num = -1
        
        if cnt == M:
            print(*answer)
            return

        for i in range(idx, N):
            if not checked[i]:
                checked[i] = 1
                answer[cnt] = numbers[i]
                NnM10(cnt + 1, i + 1, numbers[i])
                checked[i] = 0
                answer[cnt] = 0
                pre_num = numbers[i]

NnM10(0, 0, 0)