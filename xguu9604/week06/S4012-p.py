import sys
sys.stdin = open('input_S4012.txt')
from itertools import combinations

'''
요리하기 힘드네
'''

T = int(input())
cnt = 1

while T:
    N = int(input())
    # 재료간의 조합 맛의 시너지값을 받아주는 2차원배열
    table = [list(map(int, input().split())) for _ in range(N)]
    # 재료 번호를 나타내줄 리스트 생성
    gredients = [i for i in range(N)]
    # 문제에서 시너지는 20000이고 재료의 개수는 N개
    min_diff = 20000*N
    # 재료들 중에서 N/2만큼의 재료를 뽑아서 조합을 생성
    combs = combinations(gredients, N//2)
    # 만들어진 재료 조합들을 순회하면서
    for comb in combs:
        # 1번 요리의 재료를 현재 조합값으로 해주고
        g1 = list(comb)
        # 2번 요리의 재료를 받아줄 빈 리스트를 생성
        g2 = []
        # 전체 재료를 순회하면서
        for gredient in gredients:
            # 그 재료가 1번요리에서 사용되면 통과
            if gredient in g1:
                continue
            # 1번요리에서 사용되지 않았다면 2번 요리 재료에 추가
            else:
                g2.append(gredient)
        # 1번 요리의 맛
        t1 = 0
        # 2번 요리의 맛
        t2 = 0
        # 1번 요리의 재료들을 순회하면서
        for i in g1:
            for j in g1:
                # 같은 재료가 아니라면
                if i != j:
                    # 1번요리 맛 시너지에 더해준다
                    t1 += table[i][j]
        # 2번 요리도 마찬가지로 진행
        for i in g2:
            for j in g2:
                if i != j:
                    t2 += table[i][j]
        # 만약 1번요리와 2번요리의 맛차이가 최솟값보다 작다면
        if abs(t1-t2) < min_diff:
            # 최솟값을 최신화
            min_diff = abs(t1-t2)
    print(f'#{cnt} {min_diff}')
    T -= 1
    cnt += 1