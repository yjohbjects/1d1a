import sys
sys.stdin = open('input_S5099.txt')

T = int(input())
cnt = 1

while T > 0:
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    # 화덕의 피자가 다 구워진 상태를 비교해줄 리스트
    all_done = [[] for _ in range(N)]
    # 피자 리스트와 화덕 리스트의 현재 프론트값
    front_pizzas = -1
    front_fire = -1
    # 화덕 생성
    fire = [[] for _ in range(N)]
    # 마지막으로 꺼낸 피자 값을 담아줄 변수
    last_pizza = 0
    # while문으로 진입하기 위한 첫번째 조건 실행
    front_fire += 1
    front_pizzas += 1
    fire[front_fire % N] = [front_pizzas + 1, pizzas[front_pizzas]]
    # 화덕에 모든 피자의 치즈가 다 녹아서 나온 경우에 반복 종료
    while fire != all_done:
        # 화덕의 위치를 한칸 앞으로 진행
        front_fire += 1
        # 지금 확인하고 있는 화덕에 피자를 넣어줄 수 있을때
        if fire[front_fire % N] == []:
            # 피자 전부 다 구웠으면 그냥 넘어가줌
            if front_pizzas == M-1:
                continue
            # 아직 구워줘야 할 피자가 있다면 피자를 그 화덕 자리에 배치
            else:
                front_pizzas += 1
                fire[front_fire % N] = [front_pizzas+1, pizzas[front_pizzas]]
        # 화덕 칸이 비어있지 않다면
        else:
            # 우선 치즈를 반 녹여준다(화덕을 한바퀴 돌았기 때문에)
            fire[front_fire % N][1] //= 2
            # 반 녹은 치즈값이 0이라면 피자를 빼줘야한다
            if fire[front_fire % N][1] == 0:
                # 피자를 전부 다 구웠을때에는
                if front_pizzas == M - 1:
                    # 마지막으로 빼낸 피자의 번호를 마지막 피자에 최신화
                    last_pizza = fire[front_fire % N][0]
                    # 그리고 화덕을 비워준다
                    fire[front_fire % N] = []
                    continue
                # 아직 구워야 할 피자가 남아있다면
                else:
                    # 그 자리에 구워야할 피자를 다시 세팅
                    front_pizzas += 1
                    fire[front_fire % N] = [front_pizzas+1, pizzas[front_pizzas]]
            # 치즈가 덜 녹았으면 녹이기만 하고 반복 끝
            else:
                pass
    # while문 전체를 다 돌고 나서 마지막으로 뺀 피자 번호를 답으로 출력해준다.
    print(f'#{cnt} {last_pizza}')

    T -= 1
    cnt += 1