from collections import defaultdict

def solution(gems):
    gem_nums = defaultdict(int)

    # 보석의 종류 수
    n = len(set(gems))
    left = 0

    ans_list = []

    # 한개씩 확인하면서 보석의 개수를 세줌
    for right in range(len(gems)):
        gem_nums[gems[right]] += 1

        # 만약 현제 보고있는 보석의 종류가 n과 같다면
        while len(gem_nums) == n:
            # 현재 보고 있는 보석의 범위를 ans_list 에 넣어줌
            # 넣어줄땐 0-index가 아니라 1부터 시작하므로 + 1 해서 넣음
            ans_list.append([left+1, right+1])

            # 현재 보고 있는 보석 범위에서 왼쪽을 한칸 줄여줌
            # 때문에 가장 왼쪽의 보석의 갯수는 -1
            gem_nums[gems[left]] -= 1
            # 그리고 만약 이로인해 보석의 갯수가 0개가 된다면 딕셔너리에서 뺴줌
            if gem_nums[gems[left]] == 0:
                del gem_nums[gems[left]]
            # 가장 왼쪽 범위 한칸 이동
            left += 1
    # ans_list에 있는 보석의 범위중
    # 가장 짧은 구간을 return
    return sorted(ans_list,key=lambda x:(x[1]-x[0]))[0]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))