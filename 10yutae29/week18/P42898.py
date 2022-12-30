# P42898_등굣길

def solution(m, n, puddles):

    # 좌표를 기준으로 지도 만듬
    map = [[0]*(m+1) for _ in range(n+1)]
    # 계산을 편하게 하기 위해 x = 1 y = 0 좌표를 1로 저장
    map[0][1] = 1
    # 물웅덩 좌표에 -1 표시
    for puddle in puddles:
        x, y = puddle
        map[y][x] = -1

    # 좌표를 하나씩 확인할 것임
    # 현재 좌표의 왼쪽과 위쪽 좌표의 값을 더함
    # 이렇게 하면 현재 좌표까지의 최단경로 개수를 구할 수 있음
    for y in range(1, n+1):
        for x in range(1, m+1):
            # 만약 현재 좌표가 물웅덩이(-1)라면
            # 현재 좌표를 0으로 업데이트
            if map[y][x] == -1:
                map[y][x] = 0
            # 현재 좌표가 물웅덩이가 아니라면
            # 왼쪽 좌표와 오른쪽 좌표의 값을 더하여 최단경로의 갯수를 구함
            # 왼쪽좌표와 오른쪽 좌표의 값중 물웅덩이가 있다 하더라도
            # 위의 조건문을 통해 0으로 계산되었기 때문에 문제 X
            else:
                map[y][x] = map[y-1][x] + map[y][x-1]

    # 지도의 가장 오른쪽 아래(학교)까지 가는 최단 경로 갯수를 answer에 저장
    answer = map[n][m] % 1000000007

    return answer

print(solution(4, 3, [[2,2]]))