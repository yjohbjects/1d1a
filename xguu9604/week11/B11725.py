'''
메모리 때문에 1차원 배열로 연결 상태를 받아주고
그 후에는 DFS를 활용해서 연결된 친구들을 향해 쭉 나아갔음
그런데 저게 DFS가 맞나..? 코드 진행은 BFS인거 같은데 답이 나옴 ㅋㅋ
'''



N = int(input())
adj_arr = [[] for _ in range(N+1)]
# 각 노드 별로 부모 노드가 누구인지 알려주는 리스트
parent = [0]*(N+1)
# 연결 상태 기록해주고
for _ in range(N-1):
    a, b = map(int, input().split())
    adj_arr[a].append(b)
    adj_arr[b].append(a)
# 우선 0번 노드는 없는 친구니까 채워주고
parent[0] = N+1
# 1번이 루트니 시작을 위해서 값을 아무거나 채우자
parent[1] = N+1
# 스택에 루트 넣고 시작
stack = [1]
# 반복 전체 돌리고
while stack:
    # 뒤에서 하나 뽑고
    s = stack.pop()
    # 뽑은 친구와 연결된 노드들을 순회하면서
    for g in adj_arr[s]:
        # 아직 그 친구의 부모노드가 정해지지 않았을 경우에만
        if not parent[g]:
            # 그 친구 스택에 넣어주고
            stack.append(g)
            # 그 친구 부모 노드를 기록
            parent[g] = s
# 2번 노드부터 답 출력
for k in range(2, N+1):
    print(parent[k])
