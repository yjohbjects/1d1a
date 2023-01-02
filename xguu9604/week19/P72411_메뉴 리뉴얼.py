from itertools import combinations
from collections import defaultdict

'''
이터툴즈 조합으로 경우의 수 찾고
defaultdict로 경우의 수 세어준거 기록
'''

def solution(orders, course):
    answer = []
    listed = []

    # 메뉴를 문자열에서 리스트로 변환해주기
    for order in orders:
        listed.append(list(map(str, order)))

    # 시킨 메뉴를 길이 순으로 정렬하기
    # 길이 순으로 정렬하니 시간이 조금씩 단축된다는 사실!
    listed.sort(key=lambda x: len(x))
    
    # 코스 메뉴 길이별로 제일 많이 주문된 친구 찾으러 출발
    for num in course:
        # 우선 해당 길이만큼 코스 정보를 담을 딕셔너리 소환
        menus = defaultdict(int)
        # 사람들이 시킨 메뉴를 순회
        for lists in listed:
            # 그 사람이 시킨 메뉴가 코스 메뉴의 개수보다 작으면 반복을 건너 뛰자
            if len(lists) < num:
                pass
            # 그 외의 경우에는
            else:
                # 조합으로 모든 경우의 수 구하기
                combs = combinations(lists, num)
                # 그 메뉴들을 훑어 보면서
                for comb in combs:
                    # 우선 리스트로 변환해서 ('W', 'Y'), ('Y', 'W')를 통일시키자
                    comb = list(comb)
                    comb.sort()
                    # 그리고 다시 튜플로 돌려야 딕셔너리에 넣을 수 있게 된다
                    comb = tuple(comb)
                    # 해당 코스 정보 기록
                    menus[comb] += 1
                    
        # 만약에 해당 갯수만큼의 코스 요리가 존재할때
        if menus:
            # 메뉴가 나온 최댓값을 구하고
            tmp = max(menus.values())
            # 1번밖에 안나왔다면 조건에서 탈락이므로 패스
            if tmp == 1:
                pass
            # 2번 이상 나온 경우들만
            else:
                # 메뉴들을 돌면서
                for menu in menus:
                    # 제일 많이 나온 메뉴들만 찾고
                    if menus[menu] == tmp:
                        # 답에 추가해주기
                        ans = ''.join(menu)
                        answer.append(ans)
    
    # 정렬해서 값 출력
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))