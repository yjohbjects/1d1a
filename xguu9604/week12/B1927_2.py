import sys


# 힙에 값을 넣어주기
def enq(n):
    # 현재 힙에 맨 뒷번호
    global last
    # 이제 넣어줄 자리 잡아주고
    last += 1
    # 그 자리에 현재 값을 넣자
    heap[last] = n
    # 자식을 맨뒤값으로 잡고
    c = last
    # 부모는 절반
    p = c // 2
    # 부모가 있고 부모 값이 자식보다 클때 반복 계속 돌리기
    while p and heap[p] > heap[c]:
        # 자리 바꿔주고
        heap[p], heap[c] = heap[c], heap[p]
        # 부모 자식 갱신
        c = p
        p = c // 2


# 값 빼주기
def deq():
    global last
    # 반환해줄 힙의 제일 작은 값
    tmp = heap[1]
    # 맨 뒤의 값을 끌어다 와서 맨 첫값에 일단 놔두기
    heap[1] = heap[last]
    # 맨 끝값은 0으로 바꿔주자
    heap[last] = 0
    # 맨 끝값의 위치가 한칸 줄었음
    last -= 1
    # 루트부터 탐색하자
    p = 1
    # 우선 왼쪽 자식부터
    c = p * 2
    # 자식이 있는 동안은 계속 반복 진행
    while c <= last:
        # 만약 오른쪽 자식이 있고 왼자식보다 작은 값이면
        if c+1 <= last and heap[c] > heap[c+1]:
            # 오른쪽 자식으로 값을 비교
            c += 1
        # 부모가 자식보다 크면
        if heap[p] > heap[c]:
            # 자리 바꿔주고
            heap[p], heap[c] = heap[c], heap[p]
            # 부모 자식 갱신
            p = c
            c = p * 2
        # 아니면 반복 종료
        else:
            break
    # 맨 첨에 뽑았던 최솟값 반환
    return tmp


N = int(input())
# 100000번 연산하니 최소 100000개의 원소가 들어간다
heap = [0]*100000
# 힙의 제일 끝 인덱스 값
last = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    # 출력은 문제에서 주어진 대로
    if num == 0:
        if not heap[1]:
            print(0)
        else:
            print(deq())
    else:
        enq(num)