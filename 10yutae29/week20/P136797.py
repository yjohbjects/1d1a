# P136797_숫자 타자 대회

from math import log2


def solution(numbers):
    answer = 0

    # costs = [[[3,7],[2,8],[3,9]],[2]]
    # costs = [[[1,i]] for i in range(10)]
    # answer=costs

    # 플루이드 워셜

    INF = 10 ** 12
    graph = [[INF] * 10 for _ in range(10)]
    for n in range(1,10):
        if n%3 == 1:
            # costs[n].append([2,n+1])
            graph[n][n+1]=2
            if n>1:
                # costs[n].append([2,n-3])
                # costs[n].append([3,n-2])
                graph[n][n-3]=2
                graph[n][n-2]=3
            if n<7:
                # costs[n].append([2,n+3])
                # costs[n].append([3,n+4])
                graph[n][n+3]=2
                graph[n][n+4]=3
        elif n%3 == 2:
            # costs[n].append([2,n-1])
            # costs[n].append([2,n+1])
            graph[n][n-1]=2
            graph[n][n+1]=2
            if n<8:
                # costs[n].append([2,n+3])
                # costs[n].append([3,n+2])
                # costs[n].append([3,n+4])
                graph[n][n+3]=2
                graph[n][n+2]=3
                graph[n][n+4]=3
            if n>2:
                # costs[n].append([2,n-3])
                # costs[n].append([3,n-4])
                # costs[n].append([3,n-2])
                graph[n][n-3]=2
                graph[n][n-4]=3
                graph[n][n-2]=3
        else:
            # costs[n].append([2,n-1])
            graph[n][n-1]=2
            if n<9:
                # costs[n].append([2,n+3])
                # costs[n].append([3,n+2])
                graph[n][n+3]=2
                graph[n][n+2]=3
            if n>3:
                # costs[n].append([2,n-3])
                # costs[n].append([3,n-4])
                graph[n][n-3]=2
                graph[n][n-4]=3
    # costs[7].append([3,0])
    # costs[0].append([3,7])
    # costs[8].append([2,0])
    # costs[0].append([2,8])
    # costs[9].append([3,0])
    # costs[0].append([3,9])
    graph[0][7] = 3
    graph[7][0] = 3
    graph[0][8] = 2
    graph[8][0] = 2
    graph[0][9] = 3
    graph[9][0] = 3

    for i in range(10):
        graph[i][i] = 1

    for k in range(10):
        for i in range(10):
            for j in range(10):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])


    tree = [0] * (2**(len(numbers)+1))
    hand = [0] * (2**(len(numbers)+1))
    hand[1] = [4,6]
    answer = INF
    for i in range(2,len(tree)):
        left, right = hand[i//2]
        next_num = int(numbers[int(log2(i))-1])
        if i%2 == 0:
            tree[i] = tree[i//2] + graph[left][next_num]
            left = next_num
            hand[i] = [left, right]
        else:
            tree[i] = tree[i // 2] + graph[right][next_num]
            right = next_num
            hand[i] = [left, right]
        if int(log2(i)) == len(numbers) and tree[i]<answer:
            answer=tree[i]

    return answer

print(solution("151506"))

