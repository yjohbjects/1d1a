import sys

sys.stdin = open('input_S4871.txt')


T = int(input())
cnt = 1

while T > 0:
    E, V = map(int, input().split())  # V개의 경로 E개의 노드
    lst = []  # 연결되어 있는 경로를 알려주는 리스트
    result = 0  # 연결이 되어있는 길이라면 1로 결과를 출력해줄 결과값
    for i in range(V):  # 길이 V개만큼 있으므로 V번 반복
        lst.append(list(map(int, input().split())))  # 경로 리스트에 경로들 추가
        length = 0  # 조건문을 위한 리스트의 길이값을 저장할 변수
    # 리스트의 크기가 변하지 않을때까지 반복 즉 새로운 원소가 추가되지 않을때까지 반복문을 돌림
    while len(lst) != length:
        length = len(lst)  # 현재 리스트 크기값으로 변수를 최신화
        for i in range(len(lst)):  # 리스트의 원소들을 순회한다.
            for j in range(len(lst)):
                # 어떤 한 원소의 도착좌표와 다른 원소의 출발좌표가 같다 ->연결되어있는 길
                # 연결되어있는 길이 이미 리스트에 포함되어있지 않은 원소일때
                if lst[i][1] == lst[j][0] and [lst[i][0], lst[j][1]] not in lst:
                    lst.append([lst[i][0], lst[j][1]])  # 그 새로운 길을 리스트에 추가
    can_go = list(map(int, input().split()))  # 우리가 확인하고 싶은 경로값
    for path in lst:  # 리스트를 순회하면서
        if can_go == path:  # 경로가 리스트에 있는 길중에 존재한다면
            result = 1  # 결과값을 1로 바꿔주고
            break  # 반복 종료
        else:
            pass
    print(f'#{cnt} {result}')  # 답 출력력
    T -= 1
    cnt += 1