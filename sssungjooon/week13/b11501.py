# 테스트케이스 T
T = int(input())

for test_count in range(T):
    # 날의 수 N
    N = int(input())

    # 날 별 주식 가격 days
    days = list(map(int,input().split()))

    # 주식을 판매해서 최대로 얻을 수 있는 이익
    max_money = 0

    # 해당 날짜 이후의 주식이 최고가일 때의 가격
    max_price = 0

    for i in range(N-1, -1, -1):
        # 뒤부터 순회하면서 가장 해당 날짜가 가장 이득을 볼 수 있는 주식 최고가를 기록
        if days[i] > max_price:
            max_price = days[i]
        # 최고점일 때의 가격과 샀었던 주가의 가격의 차를
        # 이익에 더한다.
        max_money += max_price - days[i]

    print(max_money)