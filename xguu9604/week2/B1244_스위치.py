'''
문제 설명
임의의 개수만큼의 스위치를 제공받는다.
각 스위치는 넘버링이 되어있다.
그 후에 학생 수 만큼 값을 입력받고 각 학생은 각자의 성별과 숫자카드 한장을 받는다.
남학생은 자신이 받은 숫자 카드의 배수와 같은 번호가 적힌 스위치를 켜거나 끈다.
여학생은 자신이 받은 숫자의 전등을 기준으로 양쪽이 대칭이 끊어지는 곳까지
스위치를 켜거나 끈다.

'''




N = int(input())  # 스위치 개수

# 스위치 번호와 인덱스 값을 맞춰주기 위해 0번 인덱스 자리에 -1값 추가
on_off = [-1] + list(map(int, input().split()))
students = int(input())  # 학생 수

while students > 0:
    sex, num = map(int, input().split())  # 학생 성별과 학생이 받은 카드 숫자를 변수로 받음
    if sex == 1:  # 남학생일 경우
        # 받은 숫자 카드부터 숫자 크기단위로 순회하면서
        for i in range(num, N+1, num):
            if on_off[i] == 1:  # 켜져있으면 끄고
                on_off[i] = 0
            elif on_off[i] == 0:  # 꺼져있으면 킨다
                on_off[i] = 1
        # for i in range(1, N+1):
        #     if i % num == 0 and on_off[i] == 1:
        #         on_off[i] = 0
        #     elif i % num == 0 and on_off[i] == 0:
        #         on_off[i] = 1  이건 왜안될까
    else:  # 여학생인 경우
        sym = 0  # 대칭 거리
        while True:  # 반복을 계속 진행해준다.
            sym += 1  # 대칭 거리를 1씩 늘려가면서 확인
            if num - sym <= 0 or num + sym > N:  # 우선 인덱스 값이 기준보다 초과하게되면
                sym -= 1  # 대칭 거리를 다시 이전거리로 복귀시키고
                break  # 반복문 탈출
            else:  # 인덱스 오류가 생기지 않는 범위라면
                # 양끝이 대칭인지 확인하고 대칭이라면 문제 없이 넘긴다
                if on_off[num - sym] == on_off[num + sym]:
                    pass
                else:  # 대칭이 아니라면
                    sym -= 1  # 다시 대칭 거리를 바로 이전으로 돌려주고
                    break  # 반복문을 탈출
        for i in range(num-sym, num+sym+1):  # 받은 숫자 카드 기준으로 양옆 대칭 거리 만큼 순회하면서
            if on_off[i] == 1:  # 켜져 있으면 꺼주고
                on_off[i] = 0
            else:  # 꺼져있으면 켜준다
                on_off[i] = 1

    students -= 1

for i in range(1, N+1):  # 전체스위치를 돌아보면서
    print(on_off[i], end = " ")  # 하나씩 켜져있는지 꺼져있는지 확인
    if i % 20 == 0 :  # 20개마다 줄바꿈 한번씩 해줌줌
       print()