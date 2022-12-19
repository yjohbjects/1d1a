# P42842_카펫

def solution(brown, yellow):
    answer = []
    # 노란색 부분의 높이를 구함
    # 가장 중앙값을 찾기 위해 높이 = 노란색 격자 크기의 제곱근으로 초기설정
    height = int(yellow **(1/2))

    # 반복을 돌면서 노란색 격자의 가로 세로길이 둘다 정수가 되는 경우를 찾고
    # 그 경우에 테두리 갈색 격자의 갯수 == brown이 되면 while문 종료
    while True:
        if yellow % height == 0:
            width = yellow // height
            br_total = 2 * (width + height) + 4
            if br_total == brown:
                break
        height -= 1

    # 여기서 width와 height는 노란색 격자의 길이이므로
    # 각 +2 하여 갈색 격자를 포함한 총 카펫의 가로세로 길이를 구함
    answer.append(width+2)
    answer.append(height+2)
    return answer

b = 10
y = 2
print(solution(b, y))