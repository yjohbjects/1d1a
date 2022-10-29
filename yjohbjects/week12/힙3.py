'''
냅다 지우는 것이 아니다

우선 꺼내서 저장을 한다
마지막 노드를 삭제하면서, 맨 앞 노드로 가져온다
그리고 자식노드와의 관계 검사를 한다
'''

def enq(n):
    global last
    last += 1 # 마지막 정점 추가
    heap[last] = n # 마지막 정점에 key 추가

    c = last
    p = c // 2 # 완전이진트리에서의 부모 정점 번호

    # 부모가 없거나/ 자식 조건을 만족할 때까지
    while p and heap[p] < heap[c]:
        # 부모 < 자식인 경우 자리 교환
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    print(heap)


def deq():
    global last
    # 루트 백업
    temp = heap[1]
    
    # 삭제할 노드의 키를 루트에 복사
    heap[1] = heap[last]
    # 마지막 노드 삭제
    heap[last] = 0
    last -= 1

    # 자식과의 비교
    p = 1
    c = p * 2
    # 자식이 하나라도 있으면
    while c <= last:
        # 오른쪽 자식도 있고, 오른쪽 자신이 더 크면
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1 # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]: # 자식이 더 크면
            heap[p], heap[c] = heap[c], heap[p]
           
            # 새로운 부모/자식 번호 계산
            p = c
            c = p * 2
        else:
            break # 비교 중단

        return temp

    

heap = [0] * 100
last = 0

enq(2)
enq(5)
enq(7)
enq(4)
enq(3)
enq(6)

while last:
    print(deq())
    print(heap)
    print(last)
