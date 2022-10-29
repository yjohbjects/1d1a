# B1991 트리 순회
# https://www.acmicpc.net/problem/1991

import sys
sys.stdin = open('B1991.txt')

def preorder(start):
    global preorder_route
    preorder_route = preorder_route + tree[start][1] # self

    # left
    if tree[start][0] != '.':
        preorder(idx.find(tree[start][0]))
    # right
    if tree[start][2] != '.':
        preorder(idx.find(tree[start][2]))


def inorder(start):
    global inorder_route

    # left
    if tree[start][0] != '.':
        inorder(idx.find(tree[start][0]))

    inorder_route = inorder_route + tree[start][1]

    # right
    if tree[start][2] != '.':
        inorder(idx.find(tree[start][2]))



def postorder(start):
    global postorder_route

    # left
    if tree[start][0] != '.':
        postorder(idx.find(tree[start][0]))
    # right
    if tree[start][2] != '.':
        postorder(idx.find(tree[start][2]))

    postorder_route = postorder_route + tree[start][1]


N = int(input())
tree = [[0, 0, 0] for _ in range(N+1)]
idx = ''

for i in range(N):
    self, left, right = map(str, input().split())
    tree[i] = [left, self, right]
    idx += self

print(tree)
preorder_route = ''
preorder(0)
inorder_route = ''
inorder(0)
postorder_route = ''
postorder(0)
print(preorder_route)
print(inorder_route)
print(postorder_route)