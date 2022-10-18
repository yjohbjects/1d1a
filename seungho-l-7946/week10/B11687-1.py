# BAEKJOON 11687 -  (S3)

'''
문제
1) 가장 끝의 0의 개수가 M개인 N! 중에서 가장 작은 N을 찾는 프로그램을 작성

풀이
1) N을

입력
1) 첫째 줄에 M (1 ≤ M ≤ 100,000,000)

출력
1) 가장 끝의 0의 개수가 M개인 N! 중에서 가장 작은 N을 출력
2) 그러한 N이 없는 경우에는 -1을 출력
'''

import sys

sys.stdin = open('B11687.txt')

# input
M = int(input())


def count_zero(number):
    tmp = number
    cnt = 0
    while tmp:
        tmp //= 5
        cnt += tmp

    return cnt


def bi_search(start, end, target):
    lt = start
    rt = end
    while lt != rt:
        mid = (lt + rt) // 2
        comparison = count_zero(mid)

        if comparison >= target:
            rt = mid
        else:
            lt = mid + 1

    if count_zero(lt) == target:
        result = lt
    else:
        result = -1

    return result


# output
print(bi_search(1, 1000000000, M))
