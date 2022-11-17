# 루트 없는 트리가 주어진다. 
# 이때, 트리의 루트를 1이라고 정했을 때, 
# 각 노드의 부모를 구하는 프로그램을 작성하시오.

N = int(input())

# 트리를 만들고
tree = [[] for _ in range(0,N+1)]

# 부모 노드 기록 리스트를 만든다
parent = [0] * (N+1)

# parent의 인덱스 0과 1은 부모를 찾을 필요가 없으므로 임의 값으로 바꿔준다.
parent[0] = N*100
parent[1] = N*100

# 간선 정보를 다 기록한다.
for node_count in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

# for 문을 돌리려 했으나 1번 노드부터 순서대로 도는 것이 아닌
# 1번 노드의 자식 노드부터 차례대로 해야 올바르게 기록되므로 while 사용
# 1번 노드부터 체크하므로, 스택에 1을 넣은 채로 만든다.
stack = []
stack.append(1)

while stack :
    node = stack.pop()
    # 그 노드와 연결된 것을 트리 리스트에서 찾는다.
    for connect in tree[node] :
        # 그 연결된 노드가 부모가 없는 노드일 때
        if parent[connect] == 0 :
            # 다음 순번으로 지정해주고,
            stack.append(connect)
            # 그ꈰ고 현재 노드를 그 연결된 노드의 부모로 지정
            parent[connect] = node

# print(parent)
# 다 끝났으면, 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
for i in range(2,N+1):
    print(parent[i])