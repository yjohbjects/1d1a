import sys

N = int(sys.stdin.readline())

queue = []

for test_count in range(N):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        queue.insert(0, command[1])

    elif command[0] == "pop":
        if len(queue) != 0: 
            print(queue.pop())
        else: 
            print('-1')

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        if not queue : 
            print(1)
        else : 
            print(0)

    elif command[0] == "front":
        if len(queue) == 0: 
            print('-1')
        else: 
            print(queue[len(queue) -1])

    elif command[0] == "back":
        if len(queue) == 0: 
            print(-1)
        else: 
            print(queue[0])