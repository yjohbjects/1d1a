import sys
sys.stdin = open('in.txt')
N = int(sys.stdin.readline())

# 부모노드 i(tree_parent[i])에 자식노드와 가중치 기록?

# 자식노드 i(tree_child[i]) 부모노드와 가중치 기록
tree = [[[0, 0], [0, 0], [0, 0]] for _ in range(N + 1)]

# 이진트리의 len(간선) = len(노드) - 1
for _ in range(N - 1):
    # 부모노드, 자식노드, 거리
    # 이중연결리스트로 트리를 구현해야할듯?
    # 리스트에 [[부모, 거리], [왼쪽자식, 거리], [오른자식, 거리]]
    i, j, k = list(map(int, sys.stdin.readline().split()))

    tree[i][1]


print(tree)
max_distanace = 0
max_node = 0
    

