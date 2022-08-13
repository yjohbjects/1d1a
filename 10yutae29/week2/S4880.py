# S4880 토너먼트 카드게임

# 재귀로 카드 리스트 계속 반으로 나누고, 카드가 2개일 때 가위바위보
def half_game(card_list, win_list):
    if len(card_list) > 2 and len(card_list) % 2 == 0:  # 카드 리스트 2개 초과 일 때, 짝수일 때 a, b 반으로 나눔
        a = card_list[0:len(card_list) // 2]
        b = card_list[len(card_list) // 2::]
        return half_game(a, win_list), half_game(b, win_list)  # 재귀를 함으로써 카드 리스트가 2 또는 3이 될 때 까지 반으로 나눔

    if len(card_list) > 2 and len(card_list) % 2 == 1:  # 카드 리스트 2개 초과 일 때, 홀수일 때 a, b 반으로 나눔
        a = card_list[0:len(card_list) // 2 + 1]
        b = card_list[len(card_list) // 2 + 1::]
        return half_game(a, win_list), half_game(b, win_list)  # 재귀를 함으로써 카드 리스트가 2 또는 3이 될 때 까지 반으로 나눔

    elif len(card_list) == 2:  # 카드리스트에 2개가 있으면 가위바위보
        if (
                (card_list[0][1] == 1 and card_list[1][1] == 2)
                or (card_list[0][1] == 2 and card_list[1][1] == 3)
                or (card_list[0][1] == 3 and card_list[1][1] == 1)
        ):
            win_list.append(card_list[1])  # 승자를 승자 리스트에 추가
        elif (
                (card_list[0][1] == 2 and card_list[1][1] == 1)
                or (card_list[0][1] == 3 and card_list[1][1] == 2)
                or (card_list[0][1] == 1 and card_list[1][1] == 3)
        ):
            win_list.append(card_list[0])  # 승자를 승자 리스트에 추가
        elif card_list[0][1] == card_list[1][1]:
            win_list.append(card_list[0])  # 승자를 승자 리스트에 추가

    elif len(card_list) == 1:  # 카드 리스트가 1개일때 부전승으로 승자 리스트에 추가
            win_list.append(card_list[0])


T = int(input())  # 케이스 갯수 입력

for t in range(T):
    card_num = int(input())  # 카드 갯수 입력
    card_input = list(map(int, input().split()))  # 카드 입력
    card_list = []
    for idx, card in enumerate(card_input, start=1):
        card_list.append([idx, card])  # 학생번호와 카드를 한 리스트에 입력 ex [[1, 1], [2, 3], [3, 2], [4, 1]]

    while len(card_list) > 1:  # 카드 리스트가 1개남을때까지 즉, 우승자 1명이 나올 때까지 반복
        win_list = []  # 게임 승자리스트
        half_game(card_list, win_list)  # 재귀 설명 레츠고 ㅠ

        card_list = win_list  # 카드리스트에 승자리스트 저장 후 while 반복 계속

    print(f'#{t + 1} {card_list[0][0]}')  # 승자리스트의 [0][0]은 승자의 번호