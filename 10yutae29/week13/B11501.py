# B11501_주식
T = int(input())

for t in range(T):
    # 주식 계산할 날 수
    day = int(input())
    # 매 일마다 주식 가격
    prices = list(map(int, input().split()))
    # 뒷날부터 가장 큰 주식 가격을 구함
    right_max = 0
    # 주식 판매 금액
    benefit = 0
    for i in range(day-1, -1, -1):
        # 주식 금액이 right_max보다 높으면 right_max값을 업데이트
        if prices[i] > right_max:
            right_max = prices[i]
        # 주식은 가장 높을 때 팔아야 하니까
        # right_max에서 판매
        benefit += right_max-prices[i]
    print(benefit)