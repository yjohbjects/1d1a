import sys

sys.stdin = open('B11725.txt')

# function
def find_root(data, objective):
    if sum(data_visit) == (N - 1):
        return
    # objective = 1
    # 1 4 , 1 6 , 2 4 , 3 5 , 3 6 , 4 8
    for idx in range(len(data)):
        if objective in data[idx] and not data_visit[idx]:
            if objective == data[idx][0]:
                p = data[idx][0]
                c = data[idx][1]
            elif objective == data[idx][1]:
                p = data[idx][1]
                c = data[idx][0]
            tree[c] = p
            data_visit[idx] = 1
            find_root(data, c)

# input
N = int(input())
tree = [0] * (N + 1)

# sorted 진행
# 1 4 , 1 6 , 2 4 , 3 5 , 3 6 , 4 8
data = [sorted(list(map(int, input().split()))) for _ in range(N - 1)]
data.sort()

# visited
data_visit = [0] * (N - 1)

# root(1) 찾는 함수
find_root(data, 1)

# output
for idx in range(len(tree)):
    if idx > 1:
        print(tree[idx])