import sys

sys.stdin = open('in.txt')


def in_order(node):
    global cnt
    # 노드의 개수 N보다 큰 노드 번호는 있을 수 없다.
    if node <= N:
        in_order(node * 2)
        # 트리에 기록
        tree[node] = cnt
        cnt += 1
        in_order(node * 2 + 1)
    print(tree)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cnt = 1

    # L, R 이 없는 tree 표현
    tree = [0] * (N + 1)

    in_order(1)

    print(tree)

    tree[1]
    tree[N//2]