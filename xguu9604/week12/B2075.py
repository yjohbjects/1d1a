import sys


# 힙에 값을 넣어주는 함수
def enque(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    # 부모가 있고 부모가 자식보다 작으면 자리 바꿔주기
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


# 최대값 뽑기
def deque():
    global last
    # 리턴할 최대값
    tmp = heap[1]
    # 맨 끝값을 루트로 보내주고
    heap[1] = heap[last]
    # 리프노드 지우기
    last -= 1
    p = 1
    c = 2 * p
    # 나머지는 힙 조건 맞춰주기
    while c <= last:
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = 2 * p
        else:
            break
    return tmp


N = int(sys.stdin.readline())
last = 0
# N x N 크기의 배열이므로 0번 인덱스 제외한 길이의 리스트
heap = [0] * (N**2 + 1)
# 힙 생산
for _ in range(N):
    nums = list(map(int, sys.stdin.readline().split()))
    for num in nums:
        enque(num)
# N번째 큰 수 찾으러 ㄱ
for _ in range(N):
    answer = deque()
print(answer)
