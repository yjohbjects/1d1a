# B16236_아기 상어
from collections import Counter, deque

N = int(input())

area = []
all = []
for i in range(N):
    line = list(map(int,input().split()))
    area.append(line)
    all += line

size_count = Counter(all)
where_baby = all.index(9)
y = where_baby // N
x = where_baby % N

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

hunting_times = 0
baby_size = 2

total_time = 0
area[y][x] = 0
while True:
    visited = [[0]*N for _ in range(N)]
    visited[y][x] = 1
    queue = deque([[y, x]])
    flag = 0
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            next_y = y + dy[d]
            next_x = x + dx[d]
            if 0 <= next_y < N and 0 <= next_x < N and visited[next_y][next_x] == 0:
                if 0 < area[next_y][next_x] < baby_size:
                    total_time += visited[y][x]
                    y = next_y
                    x = next_x
                    hunting_times += 1
                    size_count[area[y][x]] -= 1
                    area[y][x] = 0
                    flag = 1

                    break
                elif area[next_y][next_x] == baby_size or area[next_y][next_x]==0:
                    queue.append([next_y, next_x])
                    visited[next_y][next_x] = visited[y][x] + 1

        if hunting_times == baby_size:
            baby_size += 1
            hunting_times = 0
        if flag == 1:
            break

    is_small = False
    for i in range(1,baby_size):
        if i in list(size_count.keys()) and size_count[i] > 0:
            break
    else:
        break

print(total_time)


