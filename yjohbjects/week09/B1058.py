# B1058 친구

N = int(input())
friends = [input() for _ in range(N)] # ['NYNNN', 'YNYNN', 'NYNYN', 'NNYNY', 'NNNYN']
connections = [[] for _ in range(N)] # [[1], [0, 2], [1, 3], [2, 4], [3]]

for i in range(len(friends)):
    for j in range(len(friends)):
        if friends[i][j] == 'Y':
            connections[i].append(j)

answer = [[] for _ in range(N)]
for i in range(len(friends)):
    for j in range(len(friends)):
        if friends[i][j] == 'Y':
            answer[i].append(j)
            for item in connections[j]:
                if item != i:
                    answer[i].append(item)

maxV = 0
for i in range(len(answer)):
    answer[i] = list(set(answer[i]))
    if len(answer[i]) > maxV:
        maxV = len(answer[i])

print(maxV)

