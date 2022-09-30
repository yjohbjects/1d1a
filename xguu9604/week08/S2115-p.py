import sys
sys.stdin = open('input_S2115.txt')

'''
여러 조건들이 많아서 조건들 때문에 계속 오답을 냈었다.
문제를 최대한 꼼꼼히 읽어보자!
이 문제의 경우 C++과 자바가 3초라서 시간적 여유가 충분할 것이라고 생각했다
그래서 그냥 전부 순회하고 찾아가는 방식으로 계산했습니다.
'''

from itertools import combinations

# 해당 지점에서의 최대 이익을 뽑아낼 수 있는 함수
def check_profit(i, j):
    # 여기서 채취할 수 있는 벌꿀의 최대 수익
    max_profit = 0
    # 벌꿀이 담겨있는 벌꿀 통
    bottles = honey[i][j:j+M]
    # 벌꿀 통에서 몇칸을 뽑아낼지에 대한 반복
    for r in range(1, M+1):
        # 벌꿀 통에서 r개의 칸을 뽑아낼 수 있는 모든 경우를 구하고
        combs = combinations(bottles, r)
        # 각 경우마다
        for comb in combs:
            # 그 경우의 꿀의 양이 최대로 담을 수 있는 양 이하라면 이익을 구해보자
            if sum(comb) <= C:
                profit = 0
                # 해당 꿀의 양을 돌면서
                for com in comb:
                    # 이익에 꿀의 양 제곱을 더해주자
                    profit += com**2
                # 그리고 최대 이익보다 크다면 갱신
                if profit > max_profit:
                    max_profit = profit
    # 마지막까지 구해서 해당 좌표에서의 최대 이익 정보를 담은 리스트를 뱉어낸다
    return [max_profit, i, j]

T = int(input())
tc = 1

while T:
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    # 각 지점에서 나올 수 있는 최대 이익들을 받아줄 리스트
    profits = []
    # 최대 이익을 뽑아내는 지점을 체킹하기 위한 방문 기록지
    checked = [[False]*N for _ in range(N)]
    # 모든 점들을 순회하면서 각 점에서의 이익 구하기
    for i in range(N):
        for j in range(N-M+1):
            profits.append(check_profit(i, j))
    # 모든 이익들을 받은 리스트를 내림차순으로 정렬
    # 각 리스트의 맨 앞의 값을 기준으로 정렬이므로 이익이 큰 순으로 정렬이 된다
    profits.sort(reverse=True)
    # 최대 이익은 그 리스트의 맨 앞의 값
    profit_1 = profits[0][0]
    # 그 다음으로 큰 이익을 나타낼 변수
    profit_2 = 0
    # 최대이익이 나오는 칸에 방문 기록을 해준다
    for k in range(M):
        checked[profits[0][1]][profits[0][2]+k] = True
    # 1씩 더해가면서 두번째로 큰 이익을 얻을 장소 탐방
    cnt = 0
    # 2번째로 가장 큰 이익을 구할때까지 반복
    while not profit_2:
        cnt += 1
        k = 0
        # 현재 탐방중인 칸이 최대 이익을 구하는 칸과 겹치는지를 알려주는 체커
        check = 0
        # 인덱스 에러 방지를 위한 조건문
        while profits[cnt][2] + k < N:
            # 해당 경우에서의 이익을 구하는 칸이 최대 이익을 구하는 칸과 겹친다면
            if checked[profits[cnt][1]][profits[cnt][2] + k]:
                # 체킹
                check = 1
                break
            # 한칸씩 옆으로 가면서 계속 확인 예정
            k += 1
            # 해당 이익을 구하는 칸을 전부 순회하면 반복 탈출
            if k == M:
                break
        # 체커가 체킹되지 않았다면 최대 이익과 겹치지 않는다는 것
        if not check:
            # 두번째 이익을 넣어주자
            profit_2 = profits[cnt][0]
    # 우리가 얻을 수 있는 최대 이익을 출력
    print(f'#{tc} {profit_1 + profit_2}')
    T -= 1
    tc += 1