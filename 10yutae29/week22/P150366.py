# P150366_표 병합

def solution(commands):
    answer = []


    # 각 cell이 다른 cell과 병합됐는지 저장하는 2차원 배열
    table = []
    # 처음에는 병합된 cell이 없으므로 각 cell은 자기 자신의 cell 번호만 가진다
    for i in range(51):
        line = []
        for j in range(51):
            line.append(set([(i,j)]))
        table.append(line)

    # 각 cell들이 가지는 값을 저장하는 2차원 배열
    # 처음에는 비어있으므로 EMPTY
    value = [['EMPTY'] * 51 for _ in range(51)]

    # 명령어를 하나씩 읽는다.
    for command in commands:

        command = command.split()


        # (y, x) cell의 값을 update하는 명령어
        if command[0] == 'UPDATE' and len(command)==4:

            # (y, x) cell과 병합된 모든 cell의 값을 주어진 value로 업데이트 해줌
            for spot in table[int(command[1])][int(command[2])]:
                y, x = spot
                value[y][x] = command[3]

        # val1 값을 가진 모든 cell을 val2로 update하는 명령어
        elif command[0] == 'UPDATE':
            val1 = command[1]
            val2 = command[2]

            # 하나씩 확인하며 val1을 val2로 바꿔줌
            for i in range(1,51):
                for j in range(1,51):
                    if value[i][j] == val1:
                        value[i][j] = val2

        # merge 명령어
        elif command[0] == 'MERGE':
            y1, x1, y2, x2 = map(int,command[1::])

            # 두 위치의 cell이 같은 cell일 경우 무시하고 넘어감
            if y1 == y2 and x1 == x2:
                continue

            # (y1, x1) cell에 값이 있다면 이 cell의 값으로 병합
            if value[y1][x1] != 'EMPTY':
                val_mer = value[y1][x1]

            # 아니라면 (y2, x2) cell 의 값으로 병합
            # (y2, x2)의 값이 'EMPTY'여도 빈 cell로 병합하는게 됨
            else:
                val_mer = value[y2][x2]

            # 만약 이 병합 이전에 각각의 cell이 병합된 상태라면
            # 서로의 병합된 cell들을 합쳐줌
            merged_spots = set(table[y1][x1].union(table[y2][x2]))

            # 위에서 합쳐진(병합된) 모든 cell들에게 병합된 값(val_mar)을 입력해줌
            # 그리고 각 cell에 병합된 cell들의 정보를 업데이트 해줌
            for merged_spot in merged_spots:
                y, x = merged_spot
                value[y][x]= val_mer
                table[y][x]=merged_spots

        # unmerge 명령어
        elif command[0] == 'UNMERGE':

            # 병합 해제할 cell
            y, x = map(int,command[1::])

            # 병합 해제할 cell과 병합 되었던 cell 정보
            merged_spots = table[y][x]

            # 병합된 cell을 하나하나씩 초기화 해줌
            for merged_spot in merged_spots:
                spot_y, spot_x = merged_spot

                # (y, x) 이외의 cell 들은 초기값 'EMPTY'로 되돌아감
                if spot_y != y or spot_x != x:
                    value[spot_y][spot_x] = 'EMPTY'

                # 병합된 모든 cell들은 초기상태로 돌아감
                # talbe에는 자기 자신의 cell 정보만 입력됨
                table[spot_y][spot_x] = set([(spot_y,spot_x)])

        # print 명령어
        elif command[0] == 'PRINT':
            # answer 리스트에 (y,x) cell의 값을 넣어줌
            y, x = map(int,command[1::])
            answer.append(value[y][x])


    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))