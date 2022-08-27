# SWEA 7701 - 염라대왕의 이름 정렬

import sys

sys.stdin = open("S7701.txt")

T = int(input())

for tc in range(1, T + 1):

    # input
    N = int(input())
    name_list = [input() for _ in range(N)]
    name_list = list(set(name_list))

    # name_number_list = []
    # for i in range(N):
    #     name_number_list.append(ord(name_list[i][0]))
    #
    # for i in range(N):
    #     min_idx = i
    #     for j in range(i + 1, N):
    #         if name_number_list[min_idx] > name_number_list[j]:
    #             min_idx = j
    #     name_number_list[i], name_number_list[min_idx] = name_number_list[min_idx], name_number_list[i]
    #
    # result = []
    # for i in range(N):
    #     for j in range(N):
    #         if name_list[j][0] == chr(name_number_list[i]):
    #             if len(result) > 0:
    #                 if result[-1] != name_list[j]:
    #                     result.append(name_list[j])
    #             else:
    #                 result.append(name_list[j])
    result = sorted(name_list, key=lambda name: (len(name),str(name)))

    print(f'#{tc}')
    for i in range(len(result)):
        print(result[i])
