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

heap = [0] * 100
last = 0

enq(1)
enq(2)
enq(1)
enq(3)
enq(3)
enq(4)
enq(3)
enq(5)
