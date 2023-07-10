import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
# [[내구도, 무게], [8, 5], ...]
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

max_eggs = 0

# 겨란 부수기 함수
# 함수내부에서 카카운트를 해줘야겟지?
def egg_breaker(idx):
    global max_eggs

    # 종료조건 1
    # 이미 젤 오른쪽 겨란을 집었다면
    if idx == N:
        # 부서진 겨란 세기
        how_many = 0
        for egg in eggs:
            if egg[0] <= 0:
                how_many += 1
        # 최대값 갱신
        max_eggs = max(how_many, max_eggs)
        # print(eggs)
        return
    else:
        # 종료조건 2
        # 든 계란이 이미 깨져있다면
        if eggs[idx][0] <= 0:
            # 다음계란으로 넘어가기
            egg_breaker(idx + 1)

        else:
            # 겨란하나씩 때려보기
            for i in range(N):
                # 조건문에 들어가면 달걀이 안깨져있다는게 증명됨
                all_eggs_broken = True

                # 나 자신이 아니고 안깨진 달걀이라면
                if i != idx and eggs[i][0] > 0:
                    # 모든 달걀 깨졋다는거 틀렸다는거 증명함
                    all_eggs_broken = False
                    # 서로 죽여라
                    eggs[idx][0] -= eggs[i][1]
                    eggs[i][0] -= eggs[idx][1]
                    # 다음 겨란을 들어라...
                    egg_breaker(idx + 1)
                    # 주겻던거 부활
                    eggs[idx][0] += eggs[i][1]
                    eggs[i][0] += eggs[idx][1]

            # 모든 달걀이 깨져있다면 = 반복문을 수행했을 때 한번도 재귀가 안일어난다면
            if all_eggs_broken:
                egg_breaker(idx + 1)

egg_breaker(0)
print(max_eggs)