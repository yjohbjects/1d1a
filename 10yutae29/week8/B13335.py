# B1335_트럭

n, w, L = map(int,input().split())

trucks = list(map(int,input().split()))
distance = [0]*n
front = -1
rear = -1
time = 1
rear += 1
distance[0] += 1
while front < n-1:

    if rear < n-1 and sum(trucks[front+1:rear+1]) + trucks[rear+1] < L:
        rear += 1
        for d in range(front+1,rear+1):
            distance[d] += 1
        time += 1
    else:
        for d in range(front+1,rear+1):
            distance[d] += 1
        time += 1

    if distance[front+1]>w:
        front += 1
        if rear < n-1:
            rear += 1
            distance[rear] += 1


print(time)
