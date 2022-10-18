# 첫째 줄 N : N+1개의 I와 N개의 O
N = int(input())
# 둘째 줄 S의 길이 M 
M = int(input())
# 셋째 줄 문자열 S
S = input()

# P_n은 I + OI * N 으로 구성되어 있다
target_P = 'I'+'OI'*N

# 글자수 세주는 카운트
count = 0

# 글자열 처음부터 훑으며 타겟P와 같은지 확인
# 이때 탐색범위는 S 전체 길이에서 타겟P 글자만큼 빼면 된다. (시작점 찾기)
for i in range(len(S)-len(target_P)):
    # I로 시작할 때
    if S[i] == 'I' :
        # i번째부터 i+타겟P의 길이만큼의 글자가 타겟P와 같다면 카운트
        if S[i:i+len(target_P)] == target_P :
            count += 1

print(count)