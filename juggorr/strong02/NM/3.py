# 중복을 허용하는 경우
# 중복 순열
# 1 2와 2 1이 다르기 때문에
import sys
N, M = map(int, sys.stdin.readline().split())

# is_in리스트가 필요없음 왜냐하면 넣은걸 또넣기도 하니깐
# 어떤 숫자가 들어갔는지 확인만 하면될듯
chosen = [0] * 10

# cnt = 숫자가 몇개 들어갔는지 세주는 변수
def NnM3(cnt):

    # 숫자를 M개 만큼 넣었으면
    if cnt == M:
        # 넣은 숫자들 뽑아주고
        for i in range(M):
            print(chosen[i], end = ' ')
        print()
        # 함수 종료
        return

    # 1부터 N + 1까지 순회하면서
    for i in range(1, N + 1):
        # 무지성으로 chosen에 넣어주기
        chosen[cnt] = i
        NnM3(cnt + 1)
        # 넣었던거 빼주는 백트래킹
        chosen[cnt] = 0

NnM3(0)