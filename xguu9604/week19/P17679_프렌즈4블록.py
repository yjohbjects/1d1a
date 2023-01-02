
# 해당 블록이 2x2로 지워지는지 확인하는 함수
def check(x, y, board):
    if board[x][y:y + 2] == board[x + 1][y:y + 2]:
        return True
    return False


'''
그냥 빡구현 해봤음 ㄹㅇ 개빡세네 빡구현
근데 뭔가 더 효율적으로 해야할 것 같긴한데 좀 채점이 관대한듯...?
'''


def solution(m, n, board):
    answer = 0
    # 우선 게임판을 다루기 쉬운 2차원 배열로 수정
    blocks = []
    for line in board:
        comps = list(map(str, line))
        blocks.append(comps)

    # 블록이 더 지워질 수 있을지 없을지 판별할 변수
    deleted = True

    # 이전에 한번이라도 블록이 지워졌다면 계속 반복 시도
    while deleted:
        # 우선 값을 초기화 해주고
        deleted = False
        # 비교해줄 게임판도 초기화를 갈겨준다
        check_board = [[0] * n for _ in range(m)]
        # 게임판의 오른쪽 벽과 바닥을 제외하고 순회를 돌자
        for i in range(m - 1):
            for j in range(n - 1):
                # 현재 블록과 오른쪽 블록이 같으면서 0이 아닌경우
                if blocks[i][j] == blocks[i][j + 1] and blocks[i][j] != 0:
                    # 해당 블록 기준으로 2x2가 지워지는지 판단하기
                    if check(i, j, blocks):
                        # 지워질 수 있는 블록이면 반복을 위해 변수값을 바꿔주고
                        deleted = True
                        # 현재 보고 있는 블록 기준으로 2x2만큼을 비교해줄 게임판에 체킹
                        for k in range(2):
                            for t in range(2):
                                check_board[i + k][j + t] = 1

        # 위의 반복을 다 돌고 비교 게임판에 체크 되어있는 곳을 확인하자
        for i in range(m):
            for j in range(n):
                # 지워진 블록들을 0으로 다 바꿔주면서 지워진 블록의 개수도 세어주기
                if check_board[i][j]:
                    blocks[i][j] = 0
                    answer += 1

        # 이제 아래로 블록을 내려주는 작업
        for j in range(n):
            # 반복 탈출을 위한 변수
            can_down = True
            while can_down:
                can_down = False
                # 맨 밑에 블록을 제외하고 열을 기준으로 행을 하나씩 확인
                for i in range(m - 1):
                    # 현재 행에 블록이 존재하고 아래 블록이 없다면
                    if blocks[i][j] and not blocks[i + 1][j]:
                        # 서로 위치를 바꿔주고
                        blocks[i][j], blocks[i + 1][j] = blocks[i + 1][j], blocks[i][j]
                        # 또 반복을 더 돌기 위해서 변수값 바꿔주기
                        can_down = True

    return answer