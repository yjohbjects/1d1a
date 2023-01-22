# BAEKJOON 2293 - 동전 1 (G5)

'''
문제
1) n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
2) 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
3) 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우

풀이
1)

입력
1) 첫째 줄에 n, k
2) 다음 n개의 줄에는 각각의 동전의 가치

출력
1) 첫째 줄에 경우의 수를 출력
'''

import sys

sys.stdin = open('B2293.txt')

def DP(num, s):

    global result

    for idx in range(num, len(coins)):

        if s == 0:
            result += 1
            return
        elif s < 0:
            return

        s -= coins[idx]
        DP(idx, s)
        s += coins[idx]

# input
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# DP
result = 0
s = K
DP(0, s)

# output
print(result)