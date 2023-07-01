import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))

answer = [0] * M
pre_num = -1

def NnM11(cnt, cur_num):
    global pre_num

    # 이전과 같은 숫자가 들어오면 종료시켜버러기
    if cur_num == pre_num:
        return
    
    else:
        pre_num = -1
        # 길이가 M이되면 출력하고 종료
        if cnt == M:
            print(*answer)
            return

        # 순회하면서
        for i in range(N):
            answer[cnt] = numbers[i]
            NnM11(cnt + 1, numbers[i])
            answer[cnt] = 0
            pre_num = numbers[i]

NnM11(0, 0)