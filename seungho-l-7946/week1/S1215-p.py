import sys
sys.stdin = open("onedayonealgorithm/week_1/input.txt", "r")

cnt = 0
while cnt != 10:
    # 10번맨
    cnt += 1
    
    # 값 입력맨
    test_cnt = 0
    test_length = int(input())
    test_case = []
    for i in range(8):
        test_case.append(list(input()))

    # 가로맨
    for i in range(8):
        for j in range(8 - test_length + 1):
            if test_case[i][j:j + test_length] == test_case[i][j:j + test_length][::-1]:
                test_cnt += 1

    # 세로맨
    for i in range(8):
        for j in range(8 - test_length + 1):
            test_vertical = ''
            for k in range(j,j + test_length):
                test_vertical += test_case[k][i]
            if test_vertical == test_vertical[::-1]:
                test_cnt += 1
    
    # 결과출력맨
    print(f'#{cnt} {test_cnt}')
