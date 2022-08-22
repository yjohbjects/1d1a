# S4871 그래프 경로

T = int(input()) # 테스트 케이스 개수

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

        before_num = len(line_infs)
        for line_idx in range(len(line_infs)):
            for line_idx2 in range(len(line_infs)):
                if (line_infs[line_idx][1] == line_infs[line_idx2][0]
                        and [line_infs[line_idx][0], line_infs[line_idx2][1]] not in line_infs):
                    line_infs.append([line_infs[line_idx][0], line_infs[line_idx2][1]])

        after_num = len(line_infs)

        if before_num == after_num:
            answer = 0
            break

    print(f'#{t+1} {answer}')