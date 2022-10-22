'''
트리를 만드는데 팔이 한개인 트리를 M개 생성해주기
M=2이면 일직선의 트리를 만들면 되지만
나머지의 경우에 끝의 노드부터 하나씩 1에다가 붙여주는 방식으로 트리 생성
'''

N, M = map(int, input().split())
# M = 2이면 그냥 일직선 트리로 만들기
if M == 2:
    for i in range(N-1):
        print(f'{i} {i+1}')
# 그 외의 경우에는
else:
    # 잘라지는 기준점을 잡기위한 변수
    diff = N - M
    # 잘라지는 노드까지는 일렬로 연결하고
    for i in range(diff+1):
        print(f'{i} {i+1}')
    # 그 뒤에 친구들은 1에다가 붙여주자
    for i in range(diff+2, N):
        print(f'1 {i}')
