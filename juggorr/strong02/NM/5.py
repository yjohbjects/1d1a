# 순열
# 추가된 조건: 1부터가 아닌 list가 주어지고 사전순으로 출력
# 해결법: 처음에 주어진 리스트를 소팅한 상태로 반복문을 돌기?
import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())

# sorted는 배열을 정렬해서 새로 만들어줌
# sort는 원래있던 배열을 정렬해버림 => 원래 있던 배열의 흔적을 찾을 수 없음
# sort는 리스트에만 적용가능하지만, sorted는 iterable이라면 다댐
nums = sorted(list(map(int, sys.stdin.readline().split())))

is_in = [0] * 10
chosen = [0] * 10

def NnM5(cnt):

    if cnt == M:
        for i in range(M):
            print(chosen[i], end=' ')
        print()

    for i in range(N):
        if not is_in[i]:
            is_in[i] = 1
            chosen[cnt] = nums[i]
            NnM5(cnt + 1)
            is_in[i] = 0
            chosen[cnt] = 0

NnM5(0)