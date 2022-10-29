# B1927 최소 힙
# https://www.acmicpc.net/problem/1927

import sys

N = int(sys.stdin.readline())
heap = [0] * (N + 1)

n = 0
for i in range(N):
    x = int(sys.stdin.readline()) # 노드 값
    if x != 0:
        n += 1 # 마지막 정점 추가
        heap[n] = x # 마지막 정점에 key 추가

        child = n
        parent = child // 2

        while parent and heap[parent] > heap[child]:
            heap[parent], heap[child] = heap[child], heap[parent]

            child = parent
            parent = child // 2

    else:
        print(heap[1])
        if heap[1] != 0:
            heap[1] = heap[n]
            heap[n] = 0
            n -= 1

            parent = 1
            child = parent * 2

            while child <= n:
                if child + 1 <= n and heap[child] > heap[child + 1]:
                    child += 1
                if heap[parent] > heap[child]:
                    heap[parent], heap[child] = heap[child], heap[parent]

                    parent = child
                    child = parent * 2
                else:
                    break

    # print(heap)