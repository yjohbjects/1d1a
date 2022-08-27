# SWEA 5097 - 회전 (D2)

import sys
sys.stdin = open("S5097.txt")

num = int(input())

for tc in range(1, num + 1):

    # input
    N, change = map(int, input().split())
    test_list = list(map(int, input().split()))

    # 나머지 계산
    result = int(change % N)

    # output
    print(f'#{tc} {test_list[result]}')