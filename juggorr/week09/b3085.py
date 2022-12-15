import sys
sys.stdin = open('in.txt')
# 가로로 캔디먹기 함수
def eat_row(arr, N):
    global maxC
    for r in range(N):
        maxC_cnt = 1
        for c in range(N - 1):
            if arr[r][c] == arr[r][c + 1]:
                maxC_cnt += 1
            # 다른색 사탕이 나오면 갯수 최댓값에 넣고
            # 다시 세기 위해 갯수 1로 초기화
            else:
                if maxC_cnt > maxC:
                    maxC = maxC_cnt
                maxC_cnt = 1
            # 끝에 도달해서 다음줄로 넘어가기전에 갯수 확인하기
            if c == N - 2:
                if maxC_cnt > maxC:
                    maxC = maxC_cnt
# 세로로 캔디먹기 함수
def eat_col(arr, N):
    global maxC
    for c in range(N):
        maxC_cnt = 1
        for r in range(N - 1):
            if arr[r][c] == arr[r + 1][c]:
                maxC_cnt += 1
            else:
                if maxC_cnt > maxC:
                    maxC = maxC_cnt
                maxC_cnt = 1
            if r == N - 2:
                if maxC_cnt > maxC:
                    maxC = maxC_cnt

N = int(input())
candies = [list(input()) for _ in range(N)]
maxC = 1
# 행에서 다른 게 등장할 때마다 바꾸고, 함수돌리고, 원위치
for r in range(N):
    for c in range(N - 1):
        if candies[r][c] != candies[r][c + 1]:
            candies[r][c], candies[r][c + 1] = candies[r][c + 1], candies[r][c]
            eat_col(candies, N)
            eat_row(candies, N)
            candies[r][c + 1], candies[r][c] = candies[r][c], candies[r][c + 1]

# 열에서도 같은 작업
for c in range(N):
    for r in range(N - 1):
        if candies[r][c] != candies[r + 1][c]:
            candies[r][c], candies[r + 1][c] = candies[r + 1][c], candies[r][c]
            eat_col(candies, N)
            eat_row(candies, N)
            candies[r + 1][c], candies[r][c] = candies[r][c], candies[r + 1][c]

print(maxC)