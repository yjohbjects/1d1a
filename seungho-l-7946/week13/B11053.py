# BAEKJOON 11053 - 가장 긴 증가하는 부분 수열 (S2)

'''
문제
1) 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성
2) 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 정답은 {10, 20, 30, 50} 이고, 길이는 4

풀이
1) Longest Increase Subsequence를 공부할 것

입력
1) 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어짐
2) 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어짐

출력
1) 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력
'''

import sys

sys.stdin = open('B11053.txt')

# input
N = int(input())
numbers = list(map(int, input().split()))

# DP 배열
# 해당 index의 숫자가 가질 수 있는 최대한의 순서를 의미함
# 기본적으로 자기자신을 첫빠따로 세울 수 있으므로 전부 1로 시작
dp = [1 for i in range(N)]

# 순회
# index별로 순회를 하는데
for i in range(N):
    
    # 해당 index까지 내부 순회를 한번 더 돔
    # 해당 index의 숫자(기준)값보다 작은 수의 갯수를 세는 것
    for j in range(i):
        
        # 기준값보다 작은 숫자가 있을 경우
        if numbers[i] > numbers[j]:
            
            # 둘 중의 큰 값을 정함
            # 기준값보다 순서값보다 1을 더해준것과 기본값을 비교
            dp[i] = max(dp[i], dp[j]+1)

# output
# 가장 큰놈 도출
print(max(dp))
