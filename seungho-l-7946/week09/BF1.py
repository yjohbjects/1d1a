# PROGRAMMERS 완전탐색 - 소수찾기

'''
문제
1) 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
2) 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return

풀이
1)

제한사항
1) numbers는 길이 1 이상 7 이하인 문자열입니다.
2) numbers는 0~9까지 숫자만으로 이루어져 있습니다.
3) "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
'''
from itertools import permutations

def solution(numbers):

    numbers = list(numbers)
    n = len(numbers)
    p_numbers = []

    for i in range(1, n + 1):
        tmp = list(permutations(numbers, i))
        for t in tmp:
            p_numbers.append(int("".join(str(r) for r in list(t))))

    p_numbers = list(set(p_numbers))

    if 1 in p_numbers:
        p_numbers.remove(1)
    if 0 in p_numbers:
        p_numbers.remove(0)

    for idx in range(len(p_numbers)):
        for x in range(2, p_numbers[idx]):
            if p_numbers[idx] % x == 0:
                p_numbers[idx] = 0
                break

    p_numbers = list(set(p_numbers))

    if 0 in p_numbers:
        p_numbers.remove(0)

    answer = len(p_numbers)

    return answer

solution("17")
solution("011")