# B1927_최소 힙
import sys
# 연산의 개수
N = int(input())

# 힙 담을 리스트
heap = [0]*200000
# 현재 힙의 마지막 인덱스
# 힙의 1번 인덱스부터 숫자를 넣을거임
last = 0


for n in range(N):
    # 연산에 대한 정보
    num = int(sys.stdin.readline())
    # 만약 num이 0이 아니면 힙에 num을 입력하는 연산
    if num:
        # num을 넣기위해 last 인덱스 값 +1
        last += 1
        # 힙 마지막 노드에 num 삽입
        heap[last] = num
        # 방금 삽입한 노드를 자식노드로 설정
        child = last
        # 그 부모노드도 구함
        parent = child // 2
        # 최소힙이기 때문에
        # 부모노드가 자식노드보다 더 크다면 서로 바꿔줘야함
        # 부모노드가 더 작을 때 까지 반복
        while heap[child] < heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            # 기존의 부모노드 위치로 간 자식노드의 부모자식관계 다시 설정
            child = parent
            parent = child // 2

    # num이 0일때 (가장 작은 숫자(1번 노드) 추출)
    else:
        # 힙에 숫자가 차있을 때
        if last:
            # 가장 작은 수 프린트
            print(heap[1])
            # 마지막 노드의 숫자를 첫번째 노드로 이동
            heap[1] = heap[last]
            heap[last] = 0

            # 마지막 노드가 첫번째 노드로 갔기 때문에 last 인덱스는 -1 된다
            last -= 1
            # 루트노드부터 자식노드와 크기비교
            parent = 1
            child = 2
            # 부모노드의 자식이 1개라도 있다면
            while child <= last:
                # 만약 자식노드가 2개가 있고 오른쪽 자식이 왼쪽자식보다 작을 때
                if child + 1 <= last and heap[child] > heap[child+1]:
                    # 더 작은 자식노드와 비교하기 위해 child 업데이트
                    child += 1
                # 부모노드가 자식노드보다 크다면 둘을 바꿔줌
                if heap[parent] > heap[child]:
                    heap[child], heap[parent] = heap[parent], heap[child]
                    # 바뀐 후 그 아래 자식노드와 비교하기 위해 parent child 업데이트
                    parent = child
                    child = parent * 2
                # 부모노드가 자식노드보다 작다면 while문 종료
                else:
                    break
        # num이 0이고 힙에 값이 없을 때 0 출력
        else:
            print(0)