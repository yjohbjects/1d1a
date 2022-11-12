# BAEKJOON 11501 - 주식 (S2)

'''
문제
1) 매일 그는 아래 세 가지 중 한 행동을 한다.
2) 주식 하나를 산다. 원하는 만큼 가지고 있는 주식을 판다. 아무것도 안한다.
3) 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁

풀이
1) 빗물 문제랑 매우 유사한 구조를 가지고 있음

입력
1) 입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어짐
2) 각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어짐
3) 둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어짐
4) 날 별 주가는 10,000이하

출력
1) 각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력
2) 답은 부호있는 64bit 정수형으로 표현 가능
'''

import sys

sys.stdin = open('B11501.txt')

# input
T = int(input())

for tc in range(T):

    N = int(input())
    stocks_price = list(map(int, input().split()))

    max_price = 0

    for idx in range(N-1, -1, -1):

        if stocks_price[idx] > max_price:
            max_price = stocks_price[idx]

        stocks_price[idx] -= max_price
        stocks_price[idx] *= -1

    # output
    print(sum(stocks_price))