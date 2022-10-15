# B1058_친구
N = int(input())

friends = [input() for _ in range(N)]

famous = 0
for i in range(N):
    f_count = 0
    visited = [0]*N

    for j in range(N):
        if friends[i][j] == 'Y' and visited[j] == 0:
            f_count += 1
            visited[j] = 1
    for k in range(N):
        if visited[k] == 1:
            for h in range(N):
                if friends[k][h] == 'Y' and h != i and visited[h] == 0:
                    f_count += 1
                    visited[h] = 2

    if famous < f_count:
        famous = f_count

print(famous)