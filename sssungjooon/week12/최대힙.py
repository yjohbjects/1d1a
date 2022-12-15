import sys
import heapq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
  m = int(sys.stdin.readline())
  if m == 0:
    if len(heap) == 0:
      print(0)
    else:
      print((-1)*heapq.heappop(heap))
  else:
    heapq.heappush(heap, (-1)*m)