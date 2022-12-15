# BAEKJOON 1932 - 정수 삼각형 (S1)

'''
문제
1) 위 그림은 크기가 5인 정수 삼각형의 한 모습
2) 맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
3) 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성
4) 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택
5) 삼각형의 크기는 1 이상 500 이하, 삼각형을 이루고 있는 각 수는 모두 정수, 범위는 0 이상 9999 이하

풀이
1) 파스칼의 삼각형 형태에서 DP를 활용

입력
1) 첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어짐

출력
1) 첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력
'''

import sys

sys.stdin = open('B1932.txt')

# input
N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]

for n in range(1, N):

    for idx in range(n + 1):
        if not idx:
            mat[n][idx] += mat[n - 1][idx]
        elif idx == n:
            mat[n][idx] += mat[n - 1][idx - 1]
        else:
            mat[n][idx] = max(mat[n][idx] + mat[n - 1][idx], mat[n][idx] + mat[n - 1][idx - 1])

# output
print(max(mat[-1]))

