# BAEKJOON 11279 - 최대힙 (S2)

'''
문제
1) 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
2) 배열에 자연수 x를 넣는다. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
3) 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

풀이
1) 구현

입력
1) 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.
2) 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
3) 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다.

출력
1) 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.
'''

import sys

sys.stdin = open('B11279.txt')

# input
N = int(sys.stdin.readline())
heap = [0] * (N + 1)
last = 0

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    if not last:
        return 0
    tmp = heap[1]
    heap[1] = heap[last]
    heap[last] = 0
    last -= 1
    p = 1
    c = p * 2
    while c >= last:
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c += 1
        if heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            break
    return tmp

for _ in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        print(deq())
    elif number > 0:
        enq(number)