from collections import Counter


def solution(topping):
    answer = 0
    # 전체 토핑의 종류와 개수를 딕셔너리 형태로 보관
    piece_1 = Counter(topping)
    # 나머지 친구의 조각은 집합으로 계산
    piece_2 = set()

    # 전체 토핑을 순회하면서
    for top in topping:
        # 반대 친구에게 토핑을 추가하고
        piece_2.add(top)
        # 내 조각에서는 그 토핑의 개수를 1개 빼주기
        piece_1[top] -= 1

        # 해당 토핑이 0개가 되면 그 토핑은 지워주기
        if not piece_1[top]:
            del piece_1[top]

        # 서로 토핑 개수가 같으면 답 체크
        if len(piece_1) == len(piece_2):
            answer += 1

    return answer

topping = [1, 2, 1, 3, 1, 2, 1, 4]
answer = solution(topping)