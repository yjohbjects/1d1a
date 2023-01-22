def preorder(n):
    print(trees[n], end='')
    if 2*n <= 26:
        if trees[2*n]:
            preorder(2*n)
    if 2*n+1 <= 26:
        if trees[2*n+1]:
            preorder(2*n+1)

def midorder(n):
    if 2*n <= 26:
        if trees[2*n]:
            midorder(2*n)
    print(trees[n], end='')
    if 2*n+1 <= 26:
        if trees[2*n+1]:
            midorder(2*n+1)

def postorder(n):
    if 2*n <= 26:
        if trees[2*n]:
            postorder(2*n)
    if 2*n+1 <= 26:
        if trees[2*n+1]:
            postorder(2*n+1)
    print(trees[n], end='')


N = int(input())
trees = [0] * 27
for i in range(N):
    p, c1, c2 = map(str, input().split())
    if i == 0:
        trees[1] = p
        trees[2] = c1
        trees[3] = c2
    else:
        num = 0
        for idx, node in enumerate(trees):
            if node == p:
                num = idx
                break
        if c1 != '.':
            trees[2*num] = c1
        if c2 != '.':
            trees[2*num + 1] = c2
preorder(1)
print()
midorder(1)
print()
postorder(1)