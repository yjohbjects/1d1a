# 수열이 오름차순 이어야 한다 = 1 2와 2 1은 같은 것
# 조합
import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))

is_in = [0] * 10
chosen = [0] * 10


# cnt = 조합에 들어간 숫자 세는 변수
# idx = 조합에 넣을 숫자 범위 조정해주는 변수
def NnM6(cnt, idx):

    # 조합에 숫자 M가 들어가면 출ㄹ력하자
    if cnt == M:
        # 고른 숫자 목록을 조합의 크기만큼 순회하면서
        for i in range(M):
            print(chosen[i], end=' ')
        print()
        return
    
    for i in range(idx, N):
        if not is_in[i]:
            is_in[i] = 1
            chosen[cnt] = nums[i]
            NnM6(cnt + 1, i)
            is_in[i] = 0
            chosen[cnt] = 0

NnM6(0, 0)