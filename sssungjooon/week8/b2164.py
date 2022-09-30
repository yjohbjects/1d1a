from collections import deque

N = int(input())

card = deque([i for i in range(1,N+1)])

while card :
    if len(card) > 1 :
        card.popleft()
        card.append(card.popleft())
    elif len(card) == 1 :
        print(card[0])
        break
