# w대의 트럭만 동시에 다리 위에 올라갈 수 있다.
# 트럭들의 무게의 합은 다리의 최대 하중 L보다 작거나 같아야 한다.

# n : 다리를 건너는 트럭의 수
# w : 다리의 길이
# L : 다리의 최대 하중

n, w, L = map(int,input().split())
# 두 번째 줄에는 트럭들의 무게
truck = list(map(int,input().split()))
bridge = [0]*w
# 건너는 시간 카운트
time_count = 0

# 다리에 트럭 리스트에 있는 트럭들이 순서대로 입장한다.
while bridge :
    time_count += 1 # 시간 1초 카운트
    bridge.pop(0) # 다리의 칸을 하나씩 줄인다.
    # 트럭이 남아있다면
    if truck:
        # 다리 최대 하중보다 현재 입장할 트럭 합친 하중이 더 크다면 빈 공간이 입장
        if sum(bridge) + truck[0] > L:
            bridge.append(0)
        # 다리 최대 하중보다 현재 입장할 트럭 합친 하중이 적으면 입장
        else:
            bridge.append(truck.pop(0))
print(time_count)