# P17679_프렌즈4블록

from collections import defaultdict
# 딕셔너리에 value값을 기본으로 설정해주는 함수


def solution(m, n, board):
    answer = 0
    # board를 문자열에서 리스트로 바꾼 후
    board = list(map(list,board))
    # 세로 단위를 쉽게 슬라이씽 하기 위해서 반시계 방향으로 90도 회전
    board = list(map(list, zip(*board)))[::-1]
    while True:
        # 각 열별 지워진 블록의 갯수를 저장할 딕셔너리
        dis_line = defaultdict(int)
        # 지울 블록의 인덱스를 저장할 set (중복 제거 필요함)
        disappear = set()

        # 순환하면서 주변 4칸이 동일하면 제거할 인덱스로 disappear에 저장
        for j in range(m-1):
            for i in range(n-1):
                # 주변 4칸이 모두 같아야 함
                # 이미 지워진 블록을 나타내는 -1은 지워질 블록에 해당되면 안됨
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != -1:
                    disappear.add((i,j))
                    disappear.add((i, j+1))
                    disappear.add((i+1, j))
                    disappear.add((i+1, j+1))

        # 더이상 지울블록 업으면 whie문 종료
        if not disappear:
            break

        # 가장왼쪽, 가장 아래부터 지우기 위해 정렬
        # 반시계 방향으로 회전시킨 지금은 가장 아래, 가장 오른쪽 부터 지우기 위해 정렬
        disappear = sorted(list(disappear),key=lambda x: -x[0])
        disappear = sorted(list(disappear),key=lambda x: -x[1])

        # 가장 밑의 블록부터 제거함
        for dis in disappear:
            y,x = dis
            # 제거할때 이전에 제거된 블록이 있어서 제거된 블록 수 만큼 칸이 내려오는것을 고려해야함

            board[y][1:x+dis_line[y]+1] = board[y][0:x+dis_line[y]]
            # 제거되어 블록이 아래로 내려가면 위쪽엔 빈 블록 표시
            board[y][0] = -1

            # 현재 열에 제거된 블록 수 + 1
            dis_line[y] += 1

    # 빈 블록 수룰 찾아서 카운트
    for j in range(m):
        for i in range(n):
            if board[i][j] == -1:
                answer+=1
    return answer


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))