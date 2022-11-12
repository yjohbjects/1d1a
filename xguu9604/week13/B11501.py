import sys

T = int(input())

while T:
    N = int(sys.stdin.readline())
    stocks = list(map(int, sys.stdin.readline().split()))
    max_stock = 0
    max_idx = 0
    profit = 0
    while max_idx < N:
        tmp = 0
        if max_idx:
            tmp = max_idx
        max_stock = max(stocks[tmp:N])
        for i, stock in enumerate(stocks):
            if stock == max_stock:
                max_idx = i
                break
        for stock in stocks[tmp:max_idx]:
            profit += max_stock - stock
        max_idx += 1
    print(profit)
    T -= 1


T = int(input())
while T:
    N = int(sys.stdin.readline())
    stocks = list(map(int, sys.stdin.readline().split()))
    max_stock = 0
    max_idx = 0
    profit = 0
    for idx, stock in enumerate(stocks):
        if stock > max_stock:
            max_stock = stock
            max_idx = idx
    for i in range(max_idx):
        profit += (max_stock - stocks[i])
    while max_idx < N:
        max_idx += 1
        max_idx_1 = max_idx
        if stocks[max_idx_1:N]:
            max_stock = max(stocks[max_idx_1:N])
        for i in range(max_idx_1, N):
            if stocks[i] == max_stock:
                max_idx = i
                break
        for j in range(max_idx_1, max_idx):
            profit += (max_stock - stocks[j])
    print(profit)
    T -= 1

import sys

T = int(input())
while T:
    N = int(sys.stdin.readline())
    stocks = list(map(int, sys.stdin.readline().split()))
    max_stock = 0
    profit = 0
    for i in range(N-1, -1, -1):
        if max_stock < stocks[i]:
            max_stock = stocks[i]
        profit += max_stock - stocks[i]
    print(profit)
    T -= 1