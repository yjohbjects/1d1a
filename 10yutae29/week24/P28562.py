

def solution(gems):
    gem_num = len(set(gems))

    group_num = gem_num

    while True:
        for i in range(0,len(gems)- group_num+1):
            group = len(set(gems[i:i+group_num]))
            if group == gem_num:
                return [i+1,i+group_num]
        else:
            group_num += 1


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(	["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))