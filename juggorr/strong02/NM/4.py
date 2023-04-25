# 중복을 허용하는 경우
# 중복 조합
# (1 2)와 (2 1)를 구분하지 않는다
import sys
N, M = map(int, sys.stdin.readline().split())

# 중복허용의 경우 is_in으로 체크해줄 필요가 없다
chosen = [0] * 10

# cnt = 조합에 숫자가 몇개 들어갔는지 확인하는 변수
# idx = 숫자를 비내림차순으로 정렬하기 위해 반복문의 시작을 정해주는 변수
def NnM4(cnt, idx):

    # 조합이 완성되면
    if cnt == M:
        # 순회하면서 차례로 출력
        for i in range(M):
            print(chosen[i], end=' ')
        print()
        # 함수 종료
        return
    
    # 조합에 숫자 넣기
    for i in range(idx, N + 1):
        chosen[cnt] = i
        NnM4(cnt + 1, i)
        chosen[cnt] = 0

NnM4(0, 1)
