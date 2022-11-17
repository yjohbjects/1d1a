import heapq

# 첫째 줄에 N이 주어진다.
N = int(input())
heap = []

for line in range(N) :
    numbers = list(map(int,input().split()))
    for number in numbers :
        # heap의 크기가 N보다 작다면 숫자 넣기
        # heap의 크기를 N으로 유지 (그래야 N번째 큰 수가 )
        if len(heap) < N :
            # heapq.heappush(heap, item)을 이용해 item을 heap에 추가
            heapq.heappush(heap, number)
        else :
            # 부모 노드의 키 값이 자식 노드의 키 값보다 작은 힙인 최소 힙 상태
            # 힙 제일 앞이 number보다 작을 경우 갈아끼워준다.
            if heap[0] < number :
                # heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 
                # 비어 있는 경우 IndexError가 호출됨. 
                heapq.heappop(heap)
                heapq.heappush(heap, number)

# 최소 힙 상태에선 제일 앞이 제일 작은 수
# 하지만 현재 heap의 크기가 N일 때는 N번째 큰 수가 된다.
print(heap[0])