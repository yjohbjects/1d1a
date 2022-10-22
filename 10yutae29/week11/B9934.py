# B9934_완전 이진 트리

# 문제의 빌딩 방문 방식은 중위 순회
# 루트 노드가 1로 시작하며, 자식노드의 크기가 +1씩 증가하는 트리와 비교


def in_order(n):
    if n < 2**K:
        in_order(2*n)
        ans.append(n)
        in_order(2*n + 1)

K = int(input())

# 상근이가 들어간 빌딩의 번호 순서
sequence = list(map(int,input().split()))

# 1부터 증가하는 트리를 중위순회한 답을 넣을 리스트
ans = []
# 루트가 1인 트리 중위순회
in_order(1)
print(ans)
# sequence와 ans를 비교하여 
# 중위순회하였을 때 sequence의 순서를 가지는 트리(real_tree)를 생성
real_tree = [0]*(2**K)
for i in range(1, 2**K):
    real_tree[ans[i-1]] = sequence[i-1]

# 트리의 1층부터 층수별로 프린트
for j in range(K):
    floor = real_tree[2**j:2**(j+1)]
    print(' '.join(map(str,floor)))