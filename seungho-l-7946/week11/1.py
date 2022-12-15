from collections import deque

def postorder(n):
    if trees[2*n]:
        postorder(2*n)
    if trees[2*n+1]:
        postorder(2*n+1)
    print(trees[n])

def make_trees(nodes):
    while nodes:
        tmp = nodes.popleft()
        idx = 1
        while True:
            if not trees[idx]:
                trees[idx] = tmp
                break
            else:
                if trees[idx] > tmp:
                    idx = 2 * idx
                else:
                    idx = 2 * idx + 1


nodes = deque()
while True:
    try:
        nodes.append(int(input()))
    except:
        break
trees = [0] * (2 ** 500)
make_trees(nodes)
postorder(1)