def solution(fees, records):
    parkingLot = {}
    temp_answer = {}
    for record in records:
        test = record.split(' ')

        # 입차
        if test[2] == 'IN':
            parkingLot[test[1]] = test[0]

        # 출차
        elif test[2] == 'OUT':
            park = parkingLot.get(test[1])
            out = test[0]

            park_hr = int(park[:2])
            park_min = int(park[3:])
            park = park_hr * 60 + park_min

            out_hr = int(out[:2])
            out_min = int(out[3:])
            out = out_hr * 60 + out_min


            # temp_answer dict에 넣어두기
            if test[1] in temp_answer:
                temp_answer[test[1]] += (out - park)
            else:
                temp_answer[test[1]] = out-park

            # 출차 후 주차장에서 삭제
            del parkingLot[test[1]]


    # 아직 주차장에 있는 차량
    for car in parkingLot:
        time = (23 * 60 + 59) - (int(parkingLot.get(car)[:2]) * 60 + int(parkingLot.get(car)[3:]))
        if car in temp_answer:
            temp_answer[car] += time
        else:
            temp_answer[car] = time

    for ans in temp_answer:
        # 기본요금
        if temp_answer.get(ans) <= fees[0]:
            temp_answer[ans] = fees[1]

        else:
            totalTime = (temp_answer.get(ans) - fees[0]) // fees[2]
            if (temp_answer.get(ans) - fees[0]) / fees[2] != (temp_answer.get(ans) - fees[0]) // fees[2]:
                totalTime = ((temp_answer.get(ans) - fees[0]) // fees[2]) + 1
            # print(temp_answer.get(ans))
            # print(totalTime)
            temp_answer[ans] = fees[1] + totalTime * fees[3]

    temp = sorted(temp_answer)
    answer = []
    for t in temp:
        answer.append(temp_answer[t])
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
