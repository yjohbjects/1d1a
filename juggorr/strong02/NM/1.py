import sys

N, M = map(int, sys.stdin.readline().split())

chosen = [0 for _ in range(10)]
is_in = [0 for _ in range(10)]

def NnM1(cnt):
    
    # 순열에 넣은 횟수를 카운트해서 M개가 되면 프린트 해주기
    if cnt == M:
        # M크기만큼 순회하면서
        for i in range(M):
            print(chosen[i], end=' ')
        # 다음줄로 이동해서 출력해주기
        print()
    
    # 1부터 순회하면서 넣었다가 빼주기 반복
    for i in range(1, N + 1):
        # 해당 숫자를 넣지 않았다면
        # is_in[i]가 0이라면
        if not is_in[i]:
            # 넣었다고 표시해주고
            # 넣은 순서대로 chosen에 넣어주기
            is_in[i] = 1
            chosen[cnt] = i
            NnM1(cnt + 1)
            # 안넣은거였다고 백트래킹해주고
            # choosen에서도 넣었던거 취소
            is_in[i] = 0
            chosen[cnt] = 0

NnM1(0)
