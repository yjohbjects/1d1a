# B1991 트리 순회

# value값이 '.'이 아닐때 자식노드가 있다는 것이므로 이때 자식노드를 순회
def pre_order(alpha):
    global pre_sequence
    pre_sequence += alpha
    if edges[alpha][0] != '.':
        pre_order(edges[alpha][0])
    if edges[alpha][1] != '.':
        pre_order(edges[alpha][1])

def in_order(alpha):
    global in_sequence
    if edges[alpha][0] != '.':
        in_order(edges[alpha][0])
    in_sequence += alpha
    if edges[alpha][1] != '.':
        in_order(edges[alpha][1])

def post_order(alpha):
    global post_sequence
    if edges[alpha][0] != '.':
        post_order(edges[alpha][0])
    if edges[alpha][1] != '.':
        post_order(edges[alpha][1])
    post_sequence += alpha

N = int(input())

# 간선정보를 딕셔너리 형태로 저장할거임
edges = {}

# {'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', 'F'], 'E': ['.', '.'], 'F': ['.', 'G'], 'D': ['.', '.'], 'G': ['.', '.']}
# e_key를 딕셔너리의 key값으로, [left, right]를 e_key에 대응하는 value값으로 저장
for n in range(N):
    e_key, left, right = list(input().split())
    edges[e_key] = [left, right]



pre_sequence = ''
pre_order('A')
print(pre_sequence)

in_sequence = ''
in_order('A')
print(in_sequence)

post_sequence = ''
post_order('A')
print(post_sequence)
