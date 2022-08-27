# S1211 Ladder2


# lad : ladder, st: starts
def down_ladder(lad, st):
    dy = [0, 0, 1]  # 좌 우 하
    dx = [-1, 1, 0]
    arrive_list = []    # 도착 시 출발한 x 인덱스와 거리를 담는 리스트
    for start in st:    # 여러개의 시작점부터 각가 탐색
        y = 0
        x = start

        visited = [[0]*100 for _ in range(100)]     # 매 시작점마다 visited가 리셋
        while y < 100:
            for move in range(3):
                ay = y + dy[move]       # 가짜 y, x를 구한 후
                ax = x + dx[move]       # 아래의 조건이 맞으면 y, x에 적용
                if (0 <= ay < 100
                        and 0 <= ax < 100
                        and visited[ay][ax] == 0
                        and lad[ay][ax] == 1):
                    visited[ay][ax] = visited[y][x] + 1     # 거리를 기록
                    y = ay      # y, x 값 업데이트(한칸 이동)
                    x = ax
                    break       # 이동 했으면 이후 불필요한 for 루프 break
            else:   #이동할 수 없으면 즉, 도착했다면
                break
        arrive_list.append([start, visited[y][x]])  # 출발점과 사다리 거리

    small = 10000   # 최솟값 초기화
    for ar_idx in range(len(arrive_list)):
        if arrive_list[ar_idx][1] <= small:     # 현재 최솟값(small)과 각 출발점 별 거리 비교
            small = arrive_list[ar_idx][1]
            ans_idx = arrive_list[ar_idx][0]
    return ans_idx



T = 10

for t in range(1, T+1):
    # 테스트 케이스 번호 받기
    tc = int(input())


    # 사다리 정보 받기
    ladder = []
    for _ in range(100):
        ladder.append(list(map(int, input().split())))

    # 시작점 찾기
    starts = []
    for idx in range(100):
        if ladder[0][idx] == 1:     # 첫번째 줄의 X인덱스만 추출
            starts.append(idx)

    print(f'#{t} {down_ladder(ladder, starts)}')
