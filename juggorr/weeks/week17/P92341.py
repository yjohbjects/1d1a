import math

def solution(fees, records):
    answer = []
    # 주차요금 정리
    basic_time = fees[0]
    basic_fee = fees[1]
    add_time = fees[2]
    add_fee = fees[3]
    
    # 문자열 records의 시각을 int로 가지는 리스트 새로 만들기
    modified_records = []
    # 바꾸는 과정에서 IN, OUT은 고려 X => 홀수 번째 등장 = IN
    # 입출차 시간을 최대 4자리 INT로 바꾸기
    for record in records:
        record = record.split(sep=' ')
        # 입출차 시각 split, join으로 네자리 string으로 바꾸고
        # int로 정수형으로 바꾸기
        record[0] = int(''.join(record[0].split(sep=':')))
        # 차량 번호도 정수형으로 바꾸기
        record[1] = int(record[1])
        # 변형레코드에 기록 추가
        modified_records.append(record)
        
    # 총 주차시간 구하기
    # 차 번호마다 dict를 만들어서 변형레코드를 순회하며
    cars_dict = {}
    for record in modified_records:
        time, car, innout = record
        
        # 차량 정보가 있다면
        if car in cars_dict:
            cars_dict[car].append(time)
        # 차량정보가 없다면 추가해주기 (기록된 시간)
        else:
            cars_dict[car] = [time]
    
    # 차량번호를 올림차순으로 sort하기 위해서 리스트로 변환
    cars_list = list(cars_dict.items())
    cars_list.sort(key=lambda x : x[0])    
    
    # 리스트를 순회하며 
    for car in cars_list:
        # 총 주차시간은 0으로 시작
        total_time = 0
        # 주차시간 기록의 갯수가 홀수면 출차가 없으므로 2359 추가
        if len(car[1]) % 2 != 0:
            car[1].append(2359)
        
        # 주차시간이 기록된 car[1]을 순회하며
        # 입차했을 경우 총 주차시간에서 빼고, 출차했을 경우 총 주차시간에 더해주기
        is_In = True
        for time in car[1]:
            if is_In:
                total_time -= time
                is_In = not is_In
            else:
                total_time += time
                is_In = not is_In
        # 요금은 기초요금으로 설정
        fee = basic_fee
        if total_time > basic_time:
            fee += math.ceil((total_time - basic_time) / add_time) * add_fee
        answer.append(fee)
        
    return answer