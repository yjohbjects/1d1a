import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
# 상담목록
cons = [(0, 0)]
# 매일 최대수익을 기록할 리스트(1일 ~ N + 1일차), 0으로 시작(index 편의)
dp = [0 for _ in range(N + 2)]

# 입력받기
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    cons.append((t, p))

# 1일차부터 ~ N일차까지
for i in range(1, N + 1):
    # i일차의 최소수입 = 전날의 수입
    if dp[i] < dp[i - 1]:
        dp[i] = dp[i - 1]

    # i일차의 상담이 퇴사전날 끝난다면 
    # ex) 7일차에 t = 1의 상담의 경우 7 + 1 <= 8 이므로 상담 가능
    if i + cons[i][0] <= N + 1:
        # 해당날짜의 dp값 vs 현재날짜 + 해당상담의 profit비교
        if dp[i + cons[i][0]] < dp[i] + cons[i][1]:
            dp[i + cons[i][0]] = dp[i] + cons[i][1]
            
print(max(dp))