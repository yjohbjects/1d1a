# 순서과 상관없으므로 조합을 찾는 문제
#1 2 == 2 1 이라는 걸 어떻게 표시할 지?
# 표시하는게 아니라 다음 반복(백트래킹 반복문)에서는 i가 2일때는
# 1을 안보면 되는 문제
# 변수명을 어떻게 잡아야 직관적?
# 봐야하는 배열의 순번을 정해준다?
# 그래서 인덱스로 변수명을 선언한건가...?
import sys

N, M = map(int, sys.stdin.readline().split())

# 해당 숫자가 조합에 들어갓는지 확인하는 배열
is_in = [0] * 10
# 조합출력을 위해 숫자를 기록해두는 배열, range(M)만큼 순회하며 조합을 출력
chosen = [0] * 10

# cnt는 조합의 길이를 재기위한 변수
# 조합의 중복여부를 체크할 변수가 하나더 필요
# 그냥 어레이를 박으면 되지만 개촌스러운 방법
# 시간도 오래걸리고 오류도 많이 나고 깊은복사, 얕은복사도 고려해야함
# idx = 1
def NnM2(cnt, idx):
    # global idx

    # 조합의 크기만큼 숫자를 넣었으면 출력해야함
    if cnt == M:
        for i in range(M):
            print(chosen[i], end=' ')
        print()
        return

    # 1부터 N까지 순회하면서 백트래킹 시행
    for i in range(idx, N + 1):
        # 아직 넣지 않은 숫자라면
        if not is_in[i]:
            # 넣었다는 표시
            is_in[i] = 1
            # 조합에 해당 숫자 넣기
            chosen[cnt] = i
            # 현재 넣은 숫자를 idx로 전달하면 해당 숫자 이후부터 넣게됨!!!!!!
            NnM2(cnt + 1, i)
            # 뺐다는 표시
            is_in[i] = 0
            # 조합에서 해당 숫자 빼기
            chosen[cnt] = 0

NnM2(0, 1)