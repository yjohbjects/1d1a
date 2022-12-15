# P92451_주차 요금 계산

# 딕셔너리의 기본값이 0인 딕셔너리 만드는 함수
from collections import defaultdict
# 숫자 올림해주는 함수
from math import ceil


def solution(fees, records):
    answer = []

    # 기본시간
    default_time = fees[0]
    # 기본 요금
    default_fee = fees[1]
    # 단위 시간
    unit_time = fees[2]
    # 단위 요금
    unit_fee = fees[3]

    # 각각의 차번호 별 총 주차시간을 딕셔너리로 저장
    # 딕셔너리의 기본값을 숫자0 으로 하기위해 defaultdict함수 사용
    time_per_car = defaultdict(int)

    # 각각 차번호 별 주차장에 입차 시간을 딕셔너리로 저장
    intime_per_car = {}

    # 입/출차 내역을 확인
    for record in records:
        time, car_num, in_out = record.split()
        # 입/출차 시간을 분(minute)로 계산
        time = int(time[0:2])*60 + int(time[3::])

        # 만약 현재 보는 기록이 '입차' 기록이라면
        # 입차 기록 딕셔너리에 key는 차 번호, value는 입차 시간을 넣어줌
        if in_out == 'IN':
            intime_per_car[car_num] = time

        # 만약 현재 보는 기록이 '출차' 기록이라면
        # 입차 기록 딕셔너리의 입차시간과 현재 기록의 출차시간을 사용해 주차시간 계산 후
        # 각 차 번호별 주차시간에 더해줌
        else:
            total_time = time - intime_per_car[car_num]
            # 차량의 입차 기록 삭제
            del intime_per_car[car_num]
            time_per_car[car_num] += total_time

    # 만약 출차 내역이 없는 차량이 있는경우 23:59분에 출차된 것으로 간주하여 주차시간 계산
    # 따라서 아직 입차 기록이 남아았는 차량을 확인
    key_nums = list(intime_per_car.keys())

    for key_num in key_nums:
        # 23:59분에 출차된 것으로 주차시간 계산
        total_time = 24*60 - 1 - intime_per_car[key_num]
        del intime_per_car[key_num]
        time_per_car[key_num] += total_time

    # 자동차 번호가 작은 차량부터 주차시간 계산해서 answer에 입력
    # key값이 자동차 번호이므로 key값을 정렬 후 for 돌릴거임
    car_nums_sorted = sorted(list(time_per_car.keys()))

    # 차량 별 주차시간에 따른 주차요금 계산
    for cn in car_nums_sorted:
        parking_time = time_per_car[cn]

        # 만약 주차시간이 기본시간보자 작다면 기본요금만 부과
        if parking_time <= default_time:
            answer.append(default_fee)
        # 주차시간이 기본시간보다 많다면 추가 요금까지 계산해서 부과
        else:
            total_fee = default_fee + ceil((parking_time - default_time)/unit_time)*unit_fee
            answer.append(total_fee)

    return answer

f = [180, 5000, 10, 600]
r = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(f, r))