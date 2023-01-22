def solution(brown, yellow):
    '''
    가운데 노란 타일을 중심으로 카펫을 확인하기
    '''
    answer = []
    # 노란타일보다 작은 수들중에 약수를 찾아가는 과정
    for i in range(1, yellow + 1):
        # 약수인 경우만 확인
        if not yellow % i:
            # 가로 길이를 지정
            j = yellow // i
            # 지금 노란 사각형을 갈색타일로 테두리를 채울 수 있는지 확인
            if 2 * (i + j) + 4 == brown:
                # 조건이 맞다면 큰 사각형 가로 세로를 차례로 추가
                # 순서대로 탐색하는 것이므로 i가 j보다 작을 수 밖에 없음
                # 따라서 j가 가로, i가 세로를 나타내는 길이가 된다.
                answer.append(j + 2)
                answer.append(i + 2)
                break
    return answer