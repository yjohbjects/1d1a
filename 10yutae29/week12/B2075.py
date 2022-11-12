# B2075_N번째 큰수

# 배열 크기와 찾아야할 N번째
N = int(input())

# 배열을 문제에 주어진 대로 만들지 않고
# 최대 힙에 입력함
# 힙 크기는 배열크기 N*N
heap = [0] * (N**2+1)
# 힙 라스트 인덱스 초기화
last = 0

# 배열 입력에서 하나씩 뽑아서 최대힙에 입력함
for n in range(N):
    for num in list(map(int,input().split())):
        last += 1
        heap[last] = num
        child = last
        parent = child // 2
        while parent and heap[child] > heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            child = parent
            parent = child // 2

# 최대힙에서 N번째 큰수를 찾기 위해서 N회 삭제
for i in range(N):
    # N번째 큰수를 찾기 위해서
    # N번쨰 반복 때 최대 힙의 첫번째 숫자 프린트
    if i == N-1:
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