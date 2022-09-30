def pre_process(P):
    lps = [0] * len(P)

    # lps를 만들기 위한 prefix에 대한 idx,
    j = 0
    # 처음부터 끝까지 순회를 돌면서
    for i in range(1, len(P)):

        # prefix idx 위치에 있는 char와 같으면 lps에 숫자 추가
        if P[i] == P[j]:
            lps[i] = j + 1
            j += 1
        # 다르다면, j(prefix index)를 초기화 해주어 pattern의 가장 처음부터 인식하도록 합니다.
        # 그 자리에서 기존의 j자리(비교를 하고 있던 자리)가 아닌 pattern 처음으로 돌아가 비교를 해줍니다.
        else:
            j = 0
            # 여기서 0으로 이동 한 prefix idx와 비교를 한번 더 해야함
            if P[i] == P[j]:
                lps[i] = j + 1
                j += 1

    return lps

def KMP(T, P):

    lps = pre_process(P)
    print(lps)

    '''
    T = 'abcdabeeabebbcdabceabeaf'
    P = 'eabea'
    '''

    # i : text를 순회하는 index
    i = 0
    # j : pattern을 순회하는 index
    j = 0

    position = -1
    while i < len(T):
        # 같으면 이동
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            # 다른데 j가 0이 아니라면, i의 자리는 유지한 채 j만 이동하여 비교 시작
            if j != 0:
                j = lps[j - 1]
            # 다른데 j가 0이라면, i를 한칸만 이동하여 처음부터 진행하듯이 진행
            else:
                i += 1
        # j가 pattern을 다 순회하면 성공
        if j == len(P):
            position = i - j
            break

    return position


T = 'abcdabeeabebbcdabceabeaf'
P = 'eabea'


position = KMP(T, P)
print(position)