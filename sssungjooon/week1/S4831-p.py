# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 
# 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 
# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 
# 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )

# 첫 줄 => 노선 수 T = 테스트 케이스 개수 (1 <= T <= 50)
T = int(input())

# 테스트 시행 (노선) 수만큼 K, N, M을 입력할 input() 반복문 만들기
# K = 한 번 충전으로 최대한 이동할 수 있는 정류장 수
# N = 종점의 번호 (지나가야할 정류장 수)
# M = 충전기가 설치된 M개의 정류장 수
for test_num in range(1,T+1):
    K, N, M = map(int, input().split())
    # 충전기의 위치를 입력할 리스트
    charge_station = list(map(int, input().split()))
    # 이제 필요한 건 충전 횟수 charge_count와 현재 위치를 나타낸 current 변수
    charge_count = 0
    current = 0

    # 종점에 도착할 때까지 반복하는 반복문을 만듦
    # 현재 위치 current에서 충전 후 최대 이동 가능 K를 더한 값이 종점 전이라면 (아직 종점 도착 전이라면)    
    while current + K < N:
        # K 범위 안에서 현 위치를 조정하면서 이동한다 (내림차순)
        for move in range(K, 0, -1):
            # 현재 위치 + 이동 거리만큼 이동했을 때 충전기가 있는 정류장일 경우
            if (current + move) in charge_station:
                # 현재 위치를 move를 더한 값으로 변경
                current += move
                # 충전 횟수 +1
                charge_count += 1
                # for 문을 종료
                break
        # 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우 charge_count를 0으로 하고 while문을 종료
        else:
            charge_count = 0
            break

    # 결과 출력
    print('#%d %d' %(test_num, charge_count))