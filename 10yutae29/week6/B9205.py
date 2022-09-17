t = int(input())

for z in range(t):
    n = int(input())
    spots = []
    for _ in range(n+2):
        spots.append(list(map(int, input().split())))
    visited = [spots[0]]
    queue = [spots[0]]
    while queue:
        x, y = queue.pop(0)
        for nx, ny in spots:
            if [nx, ny] not in visited and abs(nx - x) + abs(ny - y) <= 1000:
                visited.append([nx, ny])
                queue.append([nx, ny])
    if spots[-1] in visited:
        print('happy')
    else:
        print('sad')