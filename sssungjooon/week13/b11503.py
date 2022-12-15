# 수열의 크기 N
N = int(input())

numbers = list(map(int,input().split()))

# DP 테이블 1로 초기화
dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 가장 긴 증가하는 부분 수열의 길이값
result = max(dp)
print(result)