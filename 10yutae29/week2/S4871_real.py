# S4871 그래프 경로
# 간선의 순서가 뒤죽박죽으로 주어진 경우

T = int(input())  # 테스트 케이스 개수

for t in range(T):
    ve = list(map(int, input().split()))
    node_num = ve[0]
    ganseon = ve[1]
    line_infs = []
    for es in range(ganseon):
        line_inf = list(map(int, input().split()))
        line_infs.append(line_inf)
    sg = list(map(int, input().split()))


    while True:
        if sg in line_infs:
            answer = 1
            break
        new_line_infs = []

        for line_idx in range(len(line_infs)):
            for line_idx2 in range(line_idx+1, len(line_infs)):
                if line_infs[line_idx][1] == line_infs[line_idx2][0]:
                    new_line = [line_infs[line_idx][0], line_infs[line_idx2][1]]
                elif line_infs[line_idx][0] == line_infs[line_idx2][0]:
                    new_line = [line_infs[line_idx][1], line_infs[line_idx2][1]]
                elif line_infs[line_idx][0] == line_infs[line_idx2][1]:
                    new_line = [line_infs[line_idx][1], line_infs[line_idx2][0]]
                elif line_infs[line_idx][1] == line_infs[line_idx2][1]:
                    new_line = [line_infs[line_idx][0], line_infs[line_idx2][0]]

                if new_line not in line_infs:
                    new_line_infs.append(new_line)
        if len(new_line_infs) == 0:
            answer = 0
            break
        else:
            for new_line in new_line_infs:
                line_infs.append(new_line)

    print(f'#{t+1} {answer}')

