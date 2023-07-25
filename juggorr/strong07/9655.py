N = int(input())

# 게임을 완벽히 할 때라는 뜻은
# 어느순간 필승하는 시점이 발생한다는 뜻?

# X 1 2 3 4 5 6 7 8 9 10
# who_wins = ['X', 'SK', 'CY', 'SK', 'CY', 'SK', 'CY', 'SK']
if N % 2 == 0:
    print('CY')
else:
    print('SK')