# B14244 트리만들기

# 루트가 없는 트리이다.
# 그래서 첫번째 예시의 경우 0, 3번 노드가 리프노드가 되어 m=2를 만족한다.
# 차라리 0을 루트로 두고 m-1개의 리프노드를 가진 트리를 만들자

n, m = map(int,input().split())

tree = [[] for _ in range(n)]

# m-1개의 노드를
# 트리에서 m-1개의 노드를 제외하고 가장 작은수의 노드의 자식노드로 설정
# n = 4, m = 2이면
# 1개의 노드(3번노드)를 2번노드의 자식노드로 설정
for i in range(n-(m-1),n):
    tree[n-m].append(i)

# 이외의 노드는 자신보다 1작은 노드의 자식노드가 됨
for i in range(0, n-(m-1)-1):
    tree[i].append(i+1)


# 각 인덱스에 자식노드가 입력되어있음
# 인덱스와 그 인덱스의 리스트값을 매칭시키면 간선 정보가 됨
for idx in range(n):
    if tree[idx]:
        for t in tree[idx]:
            print(f'{idx} {t}')
    else:
        break
