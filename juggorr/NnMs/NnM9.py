import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())
numbers = sorted(list(map(int, sys.stdin.readline().split())))


checked = [0] * (N + 1)
answer = [0] * (N + 1)
pre_num = -1

def NnM9(cnt, cur_num):
    global pre_num

    # 이전과 같은 숫자가 들어왔다면 종료
    if pre_num == cur_num:
        return
    
    # 다른 숫자가 들어왔다면 이 감시체계를 일시적으로 종료시켜야 함
    else:
        pre_num = -1

    # cnt가 꽉차면 종료
    if cnt == M:
        print(*answer[: M])
        return

    for i in range(N):
        if not checked[i]:
            checked[i] = 1
            answer[cnt] = numbers[i]
            NnM9(cnt + 1, numbers[i])
            checked[i] = 0
            answer[cnt] = 0
            pre_num = numbers[i]

NnM9(0, 0)