import sys
sys.stdin = open('input_B9205.txt')

def BFS(v):
    Q = [v]
    while Q:
        current = Q.pop(0)
        for i in range(len(convs)):
            if abs(current[0]-convs[i][0])+abs(current[1]-convs[i][1]) <= 1000 and not visited[i]:
                if convs[i] == fest:
                    return 'happy'
                else:
                    Q.append(convs[i])
                    visited[i] = True
    return 'sad'

T = int(input())

while T > 0:
    n = int(input())
    home = list(map(int, input().split()))
    convs = [list(map(int, input().split())) for _ in range(n+1)]
    # fest = list(map(int, input().split()))
    fest = convs[-1]
    visited = [False] * (n+1)
    feel = BFS(home)
    print(feel)
    T -= 1