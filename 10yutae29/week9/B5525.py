# B5525_IOIOI

def pre_process(P):
    lps = [0] * len(P)

    j = 0

    for i in range(1,len(P)):

        if P[i] == P[j]:
            lps[i] = j + 1
            j += 1

        else:
            j = 0
            if P[i] == P[j]:
                lps[i] = j + 1
                j += 1
    return lps

def KMP(T,P):
    lps = pre_process(P)
    ans = 0
    # i : text를 순회하는 index
    i = 0
    # j : pattern을 순회하는 index
    j = 0


    while i < len(T):
        if P[j] == T[i]:
            i += 1
            j += 1
        else:
            # 다른데 j가 0이 아니라면, i의 자리는 유지한 채 j만 이동하여 비교 시작
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        if j == len(P):
            i = i - len(P) + 1
            j = 0
            ans += 1

    return ans



N = int(input())
M = int(input())
S = input()

comapre = 'IOI' + 'OI'*(N-1)


print(KMP(S,comapre))


