from collections import deque

'''
카드를 앞에서 빼고 그 다음카드는 맨뒤로 돌리는 
단순 작업의 코드
'''

# 인풋으로 카드의 개수만 준다
N = int(input())
# 카드 리스트를 덱으로 직접 구현하기
cards = deque([i for i in range(1, N+1)])
# 카드가 한장 남을때까지 반복
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
# 리스트에 마지막 남은 카드 뽑으며 출력
print(cards.pop())
