# 부분수열은 순서가 상관이 없기 때문에 조합임
# 하지만 조합을 1개인 것 부터 len(nums)개 까지 전부 구해야함

import sys
sys.stdin = open('in.txt')

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
# 주어진 숫자의 갯수
M = len(nums)

# S가 되면 1더해줄 변수
answer = 0

# cnt = 조합의 길이 카운트하는 변수
# idx = 조합을 만들기 위해 앞의 숫자 포함 안시키는 변수
# length = 조합의 길이를 1부터 len(sums)까지 반복문 돌리기 위한 변수
def sub(cnt, idx, long):
    global answer

    # 조합을 원하는 길이 만큼 뽑았으면
    if cnt == long:
        # 조합의 합이 S가 되는지 확인
        if sum(chosen) == S:
            answer += 1
        # 함수 종료
        return
    
    for i in range(idx, M):
        # 아직 들어있지 않으면
        if not is_in[i]:
            # 넣어주고
            is_in[i] = 1
            chosen[cnt] = nums[i]
            sub(cnt + 1, i, long)
            is_in[i] = 0
            chosen[cnt] = 0

for i in range(1, M + 1):
    
    is_in = [0] * M
    chosen = [0] * 20

    sub(0, 0, i)

print(answer)