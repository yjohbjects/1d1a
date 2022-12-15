from collections import deque
N = int(input())
Q = deque([])

for i in range(1, N + 1):
    Q.append(i)

while Q:
    v =Q.popleft()
    Q.rotate(-1)
print(v)