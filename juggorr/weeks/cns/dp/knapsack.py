import sys
sys.stdin = open('in.txt')

N, K = map(int, sys.stdin.readline().split())

stuffs = [[0, 0]]

for _  in range(N):
    w, p = map(int, sys.stdin.readline().split())
    stuffs.append([w, p])

# 무게낮은순으로 정렬
stuffs = sorted(stuffs)

# 그래프 제작
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

max_val = 0
for i in range(1, N + 1):
    for j in range(1, K + 1):

        # undefined라면 이전값을 그대로 사용하기
        if j - stuffs[i][0] < 0:
            dp[i][j] = dp[i - 1][j]

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stuffs[i][0]] + stuffs[i][1])

        max_val = max(max_val, dp[i][j])
        
print(max_val)