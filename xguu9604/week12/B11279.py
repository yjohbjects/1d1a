import sys

'''
최소 힙 문제와 같은 방식으로 힙을 구현하자!
'''


# 원소 첨가
def enq(n):
    global last
    # 원소를 추가해 줄 자리를 만들어주자
    last += 1
    # 그리고 그 리프에 해당 n을 추가
    heap[last] = n
    # 부모 자식 노드 인덱스 찾고
    p = last // 2
    c = last
    # 부모가 현재 있고 부모가 자식보다 작은 경우에 반복을 진행
    while p and heap[p] < heap[c]:
        # 부모 자식 자리 바꿔주고
        heap[p], heap[c] = heap[c], heap[p]
        # 자식과 부모 노드를 위로 올려주자
        c = p
        p = c // 2


# 원소 추출
def deq():
    global last
    # 반환 값을 따로 저장
    tmp = heap[1]
    # 맨 끝에서 루트로 숫자를 끌어오자
    heap[1] = heap[last]
    # 그리고 리프값을 지워주고
    heap[last] = 0
    # 리프 번호를 한 칸 땡겨주기
    last -= 1
    # 루트에서부터 자리 재배치 시작
    p = 1
    c = 2 * p
    # 왼쪽 자식이 존재하면 반복 진행
    while c <= last:
        # 오른쪽 자식도 있고 그녀석이 더 큰 친구라면
        if c+1 <= last and heap[c] < heap[c+1]:
            # 자식을 오른쪽으로 바꿔주자
            c += 1
        # 그리고 자식이 부모보다 크면
        if heap[c] > heap[p]:
            # 자리 바꿔주고
            heap[p], heap[c] = heap[c], heap[p]
            # 부모 자식 한칸 내려가기
            p = c
            c = 2 * p
        # 부모가 자식보다 크면 전체 반복을 탈출
        else:
            break
    # 첨에 받았던 힙의 최댓값 반환
    return tmp


N = int(input())
heap = [0] * 100000
last = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    # 0일때
    if not num:
        # 힙이 비어있으면 0 출력
        if not heap[1]:
            print(0)
        # 아니면 최댓값 출력
        else:
            print(deq())
    # 0이 아니면 힙에 넣어주기
    else:
        enq(num)