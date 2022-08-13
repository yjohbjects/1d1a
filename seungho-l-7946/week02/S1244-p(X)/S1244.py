'''
최대 상금

가장 첫 줄은 전체 테스트 케이스의 수이다.
최대 10개의 테스트 케이스가 표준 입력을 통해 주어진다.
각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.
숫자판의 정보에서 1번의 교환 횟수를 사용하여 2개의 자리수를 교환한다.
교환 횟루를 모두 소진하여, 가장 큰 수를 만들어라.
'''

import sys
sys.stdin = open("pythonProject/1algo/week02/S1244/input.txt")

num = int(input())

for tc in range(1, num + 1):

    # input
    test, N = map(int, input().split())
    test = list(str(test))

    cnt = 0

    max_test = sorted(test, reverse=True)

    while cnt != N:
        min_idx = 0
        max_idx = 0

        if test == max_test:
            while cnt != N:
                test[-1], test[-2] = test[-2], test[-1]
                cnt += 1
            break

        if cnt < len(test):
            for i in range(len(test)-1, cnt-1, -1):
                if test[max_idx] < test[i]:
                    max_idx = i

            test[cnt], test[max_idx] = test[max_idx], test[cnt]

        cnt += 1

    result = "".join(test)

    print(f'#{tc} {result}')