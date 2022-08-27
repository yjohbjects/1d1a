# S7701 염라대왕의 이름 정렬

T = int(input())

for t in range(1, T+1):
    n = int(input())    # 이름 갯수
    names = [input() for _ in range(n)]
    names = list(set(names))
    answer = sorted(names, key= lambda x : (len(x),str(x)))  # 글자수로 정렬 후, 같으면 사전순으로 정렬
    print(f'#{t}')
    for name in answer:
        print(name)






    # for i in range(len(names), 0, -1):
    #     for j in range(1, i):
    #         if len(names[j-1]) > len(names[j]):
    #             names[j-1], names[j] = names[j], names[j-1]
    #         elif len(names[j-1]) == len(names[j]):
    #             for idx in range(len(names[j])):
    #                 if names[j][idx] < names[j-1][idx]:
    #                     names[j - 1], names[j] = names[j], names[j - 1]
    #                     break
    # print(f'#{t}')
    # for name in names:
    #     print(name)
    #
    # a = sorted(names)
    #
    # print(f'#{t}')
    # for name in a:
    #     print(name)

