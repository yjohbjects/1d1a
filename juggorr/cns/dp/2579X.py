import sys

sys.stdin = open('in.txt')

N = int(sys.stdin.readline())

stairs = [0]
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

dp = [0 for _ in range(N + 1)]

# dp배열 선언하고 해당 배열의 값을 비교하며
# 최댓값으로 갱신해주면 될듯
# 첫 계단을 이동하면 무조건 첫 계단의 값을 가지게 됨
# 0 10 0 0 0 0 0 
# 최초에 두번째 계단으로 이동하면
# 0 10 20 0 0 0 0 
# 계단에서 이동할 수 있는 경우의 수는 2가지
# +1 or +2
# 하지만 이전에 +1을 2회 했을 경우 +2만 가능
# 최종 계단은 반드시 밟아야 하는 규칙
# 꼭대기 부터 내려오는 방식으로 진행해도 무리없는지?

# 한칸 이동 최근에 몇번 했는지 기록해야함
def climb(stair, point, cnt):
    
    # 종료조건
    # 최종장을 넘어갈 경우 그대로 종료
    if stair > N:
        return

    else:
        # 종료조건을 만족하지 않는다면
        # 현재 계단을 밟은 점수를 갱신시키고
        point += stairs[stair]
        # dp배열의 값과 비교해서 크다면 갱신시켜주기
        dp[stair] = max(dp[stair], point)

        # 다음이동을 진행해야 하는데 이때 연속한 계단을 이미 밟은 경우
        if cnt == 1:
            # 반드시 두칸위의 계단을 방문하고, cnt를 초기화 시켜줌
            climb(stair + 2, point, 0)

        # 아직 연속한 계단을 밟지 않은 경우
        else:
            # 한칸위로 방문할 수 도 있고
            climb(stair + 1, point, cnt + 1)
            # 두칸위로 방문도 가능
            climb(stair + 2, point, 0)


climb(0, 0, -1)

print(dp[N])