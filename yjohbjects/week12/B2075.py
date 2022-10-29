# B2075 N번째 큰 수
# https://www.acmicpc.net/problem/2075

N = int(input())

heap = [0]
for i in range(N):
    add_nums = list(map(int, input().split()))
    heap += add_nums

print(heap)
last = N * N

while last:

    child = last
    parent = child // 2

    while parent and heap[parent] < heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]

        child = parent
        parent = child // 2

    last -= 1

    print(heap)
