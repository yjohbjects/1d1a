def inorder(n):
    global cnt
    if 2*n+1 <= N:
        inorder(2*n)
    tree[n] = buildings[cnt]
    cnt += 1
    if 2*n+1 <= N:
        inorder(2*n+1)

K = int(input())
buildings = list(map(int, input().split()))
cnt = 0
N = len(buildings)
tree = [0]*(N+1)
inorder(1)
for i in range(K):
    for j in range(2**i, 2**(i+1)):
        print(tree[j], end=' ')
    print()
