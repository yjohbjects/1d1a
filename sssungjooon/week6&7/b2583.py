from collections import deque

# 눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 
# 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 
# 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    count = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < M) and (0 <= X < N) and paper[Y][X] == 0:
                paper[Y][X] = 1
                queue.append((Y, X))
                count += 1
    return count

M, N, K = map(int,input().split())

# 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 
# 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다.

# 모눈 종이를 만든다
paper = [[0]*N for _ in range(M)]

for square in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    # 그리고 그 모눈종이에 색칠을 한다 (1을 대입한다.)
    for i in range(y1,y2):
        for j in range(x1,x2):
            paper[i][j] = 1

# 빈구역
area = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 0:
            paper[i][j] = 1
            area.append(bfs(i, j))
print(len(area))
print(*sorted(area))
