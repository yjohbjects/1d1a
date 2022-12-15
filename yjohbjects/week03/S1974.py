# S1974 스도쿠 검증 D2

T = int(input())

for t in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    garo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_existG = False
    is_existS = False
    is_complete = True
    for i in range(9):
        for j in range(9):
            
            # 기준 리스트에 숫자가 존재하는지 확인
            for x in range(len(garo)):
                if sudoku[i][j] == garo[x]:
                    is_existG = True
            for y in range(len(sero)):
                if sudoku[j][i] == sero[y]:
                    is_existS = True

            # 존재한다면 리스트에서 삭제
            if is_existG:
                garo.remove(sudoku[i][j])
                is_existG = False # 불리안 초기화
                # print(garo)
            if is_existS:
                sero.remove(sudoku[j][i])
                is_existS = False # 불리안 초기화
                # print(sero)

        if len(garo) + len(sero) != 0:
            is_complete = False
            break

        # 기준 리스트 초기화
        garo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        sero = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    square = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_existSq = False
    for o in range(0, 9, 3):
        for p in range(0, 9, 3):
            for q in range(3):
                for r in range(3):
                    # print(q+o, r+p)
                    # print(sudoku[q+o][r+p])

                    # 기준 리스트에 숫자가 존재하는지 확인
                    for x in range(len(square)):
                        if sudoku[q+o][r+p] == square[x]:
                            is_existSq = True

                    # 존재한다면 리스트에서 삭제
                    if is_existSq:
                        square.remove(sudoku[q+o][r+p])
                        is_existSq = False  # 불리안 초기화

            # print(square)
            if len(square) != 0:
                is_complete = False
                break
            # print(square)
            square = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f'#{t}', 1 if is_complete == True else 0)