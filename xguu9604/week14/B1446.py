'''
이것도 다익인지는 잘 몰?루
그냥 고속도로를 전부 한칸씩 거리를 가지는 리스트로 생각해서 계산하는 방식으로 품
'''

N, D = map(int, input().split())
# 지름길에 대한 정보를 받을 리스트
# 그에 대한 정보는 해당 거리로 올수 있는 지름길의 시작점과 지름길의 거리를 인자로 받음
shortcuts = [[] for _ in range(D+1)]
for _ in range(N):
    s, g, l = map(int, input().split())
    # 지름길의 도착지점이 최종 목적지 보다 멀면 pass
    if g <= D:
        shortcuts[g].append([s, l])
# 고속도로를 정직한 거리값으로 채워준다
highway = [i for i in range(D+1)]
# 이제 고속도로를 한칸씩 나아가며 운전 ㄱㄱ
for idx in range(D+1):
    # 현재 고속도로로 올수 있는 거리를 이전 칸 +1과 현재 칸과의 최솟값으로 바꿔주기
    highway[idx] = min(highway[idx-1]+1, highway[idx])
    # 현재 지점으로 연결되어있는 지름길이 있다면
    if shortcuts[idx]:
        # 지름길들을 다 비교해보자
        for shortcut in shortcuts[idx]:
            # 지름길로 오는 길이랑 현재 찍혀있는 길이랑 비교해서 짧은 놈으로
            highway[idx] = min(highway[shortcut[0]] + shortcut[1], highway[idx])
# 끝까지 다 올때 최소거리가 도착지점의 값
print(highway[-1])