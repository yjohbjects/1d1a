# BAEKJOON 2294 - 동전 2 (G5)

'''
문제
1) n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
2) 그러면서 동전의 개수가 최소가 되도록 하려고 한다. 각각의 동전은 몇 개라도 사용할 수 있다.

풀이
1) DP 활용

입력
1) 첫째 줄에 n, k (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
2) 다음 n개의 줄에는 각각의 동전의 가치
3) 가치가 같은 동전이 여러 번 주어질 수도 있다.

출력
1) 첫째 줄에 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력
'''

import sys

sys.stdin = open('B2294.txt')

# input
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

# DP
INF = 1000000
D = [INF] * INF
D[0] = 0
for idx in range(K):
    for coin in coins:
        D[idx + coin] = min(D[idx + coin], D[idx] + 1)

# output
if D[K] != INF:
    print(D[K])
else:
    print(-1)