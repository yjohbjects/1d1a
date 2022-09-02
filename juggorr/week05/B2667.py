import sys
sys.stdin = open('B2667.txt')

def BFS(r, c):
    queue = []
    queue.append((r, c))
    global count
    nums = 0
    # 단지가 있고 / 방문한적 없다면
    if maat[r][c] == 1 and maap[r][c] == 0:
        # 새로운 단지이기 때문에 단지번호 1더하기
        count += 1
        maap[r][c] = count
        # 단지 수세기 위한 변수
        nums += 1

        while queue:
            r, c = queue.pop(0)
            # 델타이동
            for i in range(4):
                nc, nr = c + dx[i], r + dy[i]
                # 행렬 내부이고 / 단지가 있고 / 방문한 적이 없다면
                if (
                    0 <= nr < N
                    and 0 <= nc < N
                    and maat[nr][nc] == 1
                    and maap[nr][nc] == 0
                ):
                    queue.append((nr, nc))
                    # 단지수 세기
                    nums += 1
                    # 현재 단지수 붙이기
                    maap[nr][nc] = count
    return nums

N = int(input())
# 행렬 입력받기
maat = [list(map(int, input())) for _ in range(N)]
maap = [[0] * N for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 0
# 각 단지수 세기 위한 빈 리스트
total_nums = []

# BFS 돌리기
for r in range(N):
    for c in range(N):
        total_nums.append(BFS(r, c))

# 총 단지수 출력
print(count)

# 오름차순 정렬 출력
total_nums.sort()
for num in total_nums:
    if num != 0:
        print(num)