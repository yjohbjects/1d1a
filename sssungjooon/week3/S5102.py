import sys
sys.stdin = open("5102.txt")

# V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
# 주어진 출발 노드에서 최소 몇 개의 간선을 지나면
# 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
# 노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.

# 우선 너비탐색 함수 BFS부터 정의해준다.
# BFS 함수
#BFS 함수
def bfs(queue):
    # 지나야할 간선 최소 개수 count 먼저 언급 (기본값은 1)
    count = 1
    #큐가 빌때까지 반복
    while queue:
        # 2개의 큐가 필요하므로 한개 더 생성한다.
        s_queue = []
        #큐가 빌 때까지 반복한다.
        while queue:
            #원소를 꺼내서 인덱스로 저장한다.
            idx = queue.pop()

            #연결되어 있는 부분들을 확인한다.
            for i in connect[idx]:
                #이미 방문했다면 넘어간다.
                if visited[i] == 1:
                    continue

                #도착지와 일치한다면 이동거리를 반환한다.
                if i == end:
                    return count
                #위의 조건에 걸리지 않는다면 두번재 큐에 추가한다.
                s_queue.append(i)
                #방문처리를 한다.
                visited[i] = 1
        #모든 큐가 비었다면 카운트를 증가시킨다.
        count += 1
        #큐를 교체한다.
        queue = s_queue
    #여기까지 왔다면 목적지까지 도착할 수 없다.
    return 0

# 함수 정의가 끝났으면 테스트 케이스 완성하기
T = int(input())

for test_count in range(1, T+1) :
    # 노드 개수 V와 간선 개수 E
    V, E = map(int, input().split())

    # 간선 연결 표시할 리스트 connect를 만든다.
    # 이를 통해서 연결된 상태를 확인할 수 있다.
    # 범위가 V+1인 이유는 0부터가 아닌 노드 번호 그대로 V번까지 되도록
    connect = [[] for _ in range(V + 1)]

    # connect 안에 들어갈 데이터를 편집한다.
    for i in range(E):
        a, b = map(int, input().split())
        connect[a].append(b)
        connect[b].append(a)

    # 방문여부를 기록할 visited (0 = 방문X / 1 = 방문 처리)
    visited = [0 for _ in range(V + 1)]

    # 시작노드와 끝나는 노드 저장
    start, end = map(int, input().split())

    # 시작노드 미리 방문 처리를 해놓는다.
    visited[start] = 1

    # bfs 함수 돌려서 출력하기
    print(f'{test_count} {bfs([start])}')

    # print(connect)
