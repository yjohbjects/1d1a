# B1300_K번째 수

# 배열의 크기
N = int(input())
# 찾아야할 B원소의 인덱스
k = int(input())

# 배열 A를 만들지 말고
# 배열 A에 들어갈 값을 바로 힙에 입력
heap = [0] * (N**2+1)
last = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        num = i*j
        last += 1
        heap[last] = num
        child = last
        parent = child // 2
        while parent and heap[child] > heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent
            parent = child // 2

# 오름차순으로 정렬된 행렬 B에서 B[k]를 찾는 것은
# B에서 N**2 - k 번째로 큰 숫자를 찾는거와 같음
# 최대힙에서 N**2 - k번째 큰수를 찾기 위해서 N**2 - k회 삭제
for i in range(N**2 - k):
    # N번째 큰수를 찾기 위해서
    # N번쨰 반복 때 최대 힙의 첫번째 숫자 프린트
    if i == N**2 - k - 1:
        print(heap[1])
        break
    # 1 ~ N-1 때는 힙에서 삭제연산
    else:
        heap[1] = heap[last]
        heap[last] = 0
        last -= 1
        parent = 1
        child = 2
        while child <= last:
            if child + 1 <=last and heap[child] < heap[child+1]:
                child += 1
            if heap[child] > heap[parent]:
                heap[child], heap[parent] = heap[parent], heap[child]
                parent = child
                child = parent * 2
            else:
                break