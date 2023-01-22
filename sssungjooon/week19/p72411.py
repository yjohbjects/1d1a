from itertools import combinations
from collections import Counter

# 기존에 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴로 제공
# 각 손님들이 주문할 때 가장 많이 함께 주문한 단품 메뉴들을 코스 요리 메뉴로 구성
# 코스요리 메뉴는 최소 2가지 이상의 단품 메뉴로 구성
# 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기
# orders => 각 손님들이 주문한 단품 메뉴들이 문자열 형식으로 담김
# course => 코스요리를 구성하는 단품 메뉴들의 개수

def solution(orders, course):
    answer = []

    # 순서를 생각하지 않고, [B,A,C], [A,B,C]를 같은 것으로 보기 때문에 조합을 사용한다
    # 코스 개수별로 for문을 돈다
    for c in course :
        # 코스 개수별 menu 리셋
        menu = []
        # 각 손님별로 for문을 돈다.
        for order in orders :
            # 코스의 요리 개수만큼 조합 생성
            # combinations(세트, 몇개를 뽑을지)
            menu_case = list(combinations(sorted(order),c))
            menu += [case for case in menu_case]
        count_menu = Counter(menu)
        if len(count_menu) != 0 and max(count_menu.values()) != 1 :
            answer += [''.join(i) for i in count_menu if count_menu[i] == max(count_menu.values())]

    return sorted(answer)

