import sys
sys.stdin = open('2.txt')
############위에 지우기##############

T = int(input())
for t in range(1, T + 1):
    # input
    Ms, Ma = map(int, input().split()) # 예치금 / 월별 불입 금액
    N, L =  map(int, input().split()) # 종목 수 / 과거 데이터 기간
    stock = [[] for _ in range(N)]
    for i in range(N):
        stock[i] = list(map(int, input().split()))


    balance = Ms
    diff = [[] for _ in range(N)]
    stock_howmany = 0
    stock_wallet = [0 for _ in range(N)]
    for i in range(L): # 한달
        # print(balance)

        # 이번달 주식가
        stock_thismonth = [stock[x][i] for x in range(N)]

        if i != 0:
            balance += Ma # 월별 불입 금액 저축

        # 전달에 매수한 주식이 있다면
        if sum(stock_wallet) != 0:
            for y in range(N):
                balance += stock_thismonth[y] * stock_wallet[y]
                stock_wallet[y] = 0

        # 다음달과의 차이를 저장
        for j in range(N):
            if stock[j][i] >= stock[j][i + 1]:
                diff[j] = 0
                stock_thismonth[j] = 100000
            else:
                diff[j] = stock[j][i + 1] - stock[j][i]

        # 다음달에 오르는 종목이 없을 때
        if diff.count(0) == N:
            continue

        # 다음달에 오르는 종목이 있을 때

        while True:
            # 수익률이 가장 좋은 주식 종목 넘버 중에서도 가장 싼 주식 구매
            if diff.count(max(diff)) > 1:
                minV = 100000
                for z in range(len(diff)):
                    if diff[z] == max(diff) and diff[z] < minV:
                        stock_idx = z
            else:
                stock_idx = diff.index(max(diff))

            # 살 수 있는 주식이라면 매수
            if stock_thismonth[stock_idx] <= balance:
                balance -= stock_thismonth[stock_idx]
                stock_wallet[stock_idx] += 1
                # print('매수', stock_idx, stock_thismonth[stock_idx])
            # 살 수 없다면 수익액 초기화
            else:
                diff[stock_idx] = 0
                
            # 아무 주식도 살 수 없는 잔고라면 break
            if balance < min(stock_thismonth):
                break

    # 마지막날
    balance += Ma  # 월별 불입 금액 저축
    # 종목이 있으면 매도하고 끝
    if sum(stock_wallet) != 0:
        for y in range(N):
            balance += stock[y][L] * stock_wallet[y]

    # print(balance)
    print(f'#{t} {balance - (Ms + (Ma * L))}')