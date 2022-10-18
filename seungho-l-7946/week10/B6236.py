# BAEKJOON 6236 - 용돈 관리 (S2)

'''
문제
1) 현우는 앞으로 N일 동안 자신이 사용할 금액을 계산하였고, 돈을 펑펑 쓰지 않기 위해 정확히 M번만 통장에서 돈을 빼
2) K원을 인출하며, 통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용하고, 모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출
3) 정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출
4) 인출 금액 K를 최소화하기로 하였다. 현우가 필요한 최소 금액 K를 계산하는 프로그램

풀이
1) 이진 탐색 구현.. 인데 굉장히 어렵네욧

입력
1) 1번째 줄에는 N과 M이 공백
2) 2번째 줄부터 총 N개의 줄에는 현우가 i번째 날에 이용할 금액

출력
1) 첫 번째 줄에 현우가 통장에서 인출해야 할 최소 금액 K를 출력
'''

import sys

sys.stdin = open('B6236.txt')

# input
N, M = map(int, input().split())
can_use = [int(input()) for _ in range(N)]

# 결과값, 최소/최대 설정
result = 0
min_K = max(can_use)
max_K = sum(can_use)

# 이진 탐색 종료 조건
while min_K <= max_K:

    # 초기화 값
    start_K = (max_K + min_K) // 2
    withdrawal = start_K
    cnt = 1

    # 나가는 돈이 더 많으면 뽑아버리기
    for idx in range(len(can_use)):
        if withdrawal < can_use[idx]:
            withdrawal = start_K
            withdrawal -= can_use[idx]
            cnt += 1
        else:
            withdrawal -= can_use[idx]

    # 초기화 조건
    if cnt > M:
        min_K = start_K + 1
    elif cnt <= M:
        max_K = start_K - 1

# output
print(start_K)