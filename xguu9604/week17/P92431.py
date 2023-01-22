def solution(fees, records):
    answer = []
    # 현재 주차되어있는 차량
    parking = {}
    # 차량별로 사용시간
    used_time = {}
    # 차량별로 내야할 요금
    pay_for = {}

    for record in records:
        time, car, status = record.split()
        # 차가 들어오면 주차장에 추가
        if status == "IN":
            parking[car] = time
        # 차가 나가는 경우 사용시간을 계산
        else:
            out_time = time
            in_time = parking[car]
            out_h, out_m = map(int, out_time.split(':'))
            in_h, in_m = map(int, in_time.split(':'))

            if in_m > out_m:
                out_h -= 1
                out_m += 60

            if car in used_time:
                used_time[car] += out_m - in_m + 60 * (out_h - in_h)
            else:
                used_time[car] = out_m - in_m + 60 * (out_h - in_h)
            # 주차장에서 차를 제거
            del parking[car]

    # 아직 차가 남아있다면 마감시간 기준 사용시간 계산
    if parking:
        for car in parking:
            in_h, in_m = map(int, parking[car].split(":"))
            out_h, out_m = 23, 59

            if car in used_time:
                used_time[car] += out_m - in_m + 60 * (out_h - in_h)
            else:
                used_time[car] = out_m - in_m + 60 * (out_h - in_h)

    # 사용 시간을 기준으로 금액 계산
    for car in used_time:
        if used_time[car] <= fees[0]:
            pay_for[car] = fees[1]
        else:
            if (used_time[car] - fees[0]) % fees[2]:
                pay_for[car] = fees[1] + (((used_time[car] - fees[0]) // fees[2]) + 1) * fees[3]

            else:
                pay_for[car] = fees[1] + ((used_time[car] - fees[0]) // fees[2]) * fees[3]

    # 차량 번호 기준으로 정렬
    pay_for = sorted(pay_for.items())
    for i, cost in pay_for:
        answer.append(cost)
    return answer

print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))