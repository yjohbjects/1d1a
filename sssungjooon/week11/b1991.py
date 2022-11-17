# 먼저 전위순회, 중위순회, 후위순회 함수를 만들어 놓자
def preorder(root):
    if root != '.' :
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.' :
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.' :
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

T = int(input())

# 트리를 만들자
# 다만 A, B, C처럼 알파벳의 형태라 순서가 따로 없으므로
# 리스트가 아닌 딕셔너리로 저장되게 만들어야 한다.
tree = {}

for test_count in range(T):
    parent, left, right = input().split()
    tree[parent] = [left, right]

# print(tree)

# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다.
# 항상 A가 루트 노드이므로, 루트 노드부터 순회한다.
preorder('A')
print()
inorder('A')
print()
postorder('A')

