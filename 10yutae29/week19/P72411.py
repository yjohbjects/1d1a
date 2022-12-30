# P72411_메뉴 리뉴얼

from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    answer = []

    sets_count = defaultdict(int)
    for cor in course:
        for order in orders:
            if len(order) >= cor:
                print(list(combinations(order,cor)))

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))