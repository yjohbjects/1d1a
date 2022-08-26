import sys
sys.stdin = open('input_B10158.txt')

# 판의 가로 세로 길이를 받아옴
W, H = map(int, input().split())
# 시작 점의 좌표를 잡아줌
start = list(map(int, input().split()))
# 개미녀석이 움직이는 시간
hour = int(input())
# 세로든 가로든 길이의 두배의 시간이 지나가면 제자리이다
# 나머지를 구해서 계산을 용이하게 하기 위해 세로 가로 시간을 따로 나눈다
w_hour = hour % (2*W)
h_hour = hour % (2*H)
# 가로로 주어진 시간 만큼 이동했을때 가로를 뚫고 간다면
if start[0] + w_hour > W:
    # 가로의 좌표는 아래의 식과 같은 위치에 존재한다
    start[0] = abs((start[0]+w_hour)-2*W)
# 가로를 뚫지 못하면
else:
    # 그냥 그 시간을 더해준다
    start[0] += w_hour
# 세로도 마찬가지로
if start[1] + h_hour > H:
    start[1] = abs((start[1]+h_hour)-2*H)
else:
    start[1] += h_hour
# 도착 좌표 출력
print(start[0], end=' ')
print(start[1])
