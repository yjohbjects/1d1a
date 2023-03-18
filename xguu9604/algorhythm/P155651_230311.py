def solution(book_time):
    answer = 0
#   예약 시간을 시간 순으로 정렬하기
    book_time.sort()
#   현재 가용가능한 방을 받아줄 리스트
    rooms = []
#   이제 예약 테이블 만들어보자
    for time in book_time:
#       우선 현재 예약 시간이 예약이 되었는지 판단해줄 지표
        booked = False
#       대실 시작 시간과 끝나는 시간을 나눠주고
        start_time, end_time = time
#       시작 시간과 분을 나눠주자
        start_hour, start_min = start_time.split(":")
        end_hour, end_min = end_time.split(":")
        
#       나눈 친구들 기준으로 분단위로 시간을 치환하자
        start_T = int(start_hour) * 60 + int(start_min)
#       퇴실 시간에는 그냥 청소 시간까지 계산을 미리 다 해버리자
        end_T = int(end_hour) * 60 + int(end_min) + 10
        
#       아직 대실한 방이 없으면 우선 방을 하나 만들어주자
        if not rooms:
            rooms.append(end_T)
#       그 외에 방이 있는 경우에는
        else:
#           현재 가용가능한 방을 다 둘러보면서
            for i in range(len(rooms)):
#               지금 보고있는 예약이 방이 배정되었으면 반복은 멈추고
                if booked:
                    continue
#               아직 방 배정이 안되었다면
                else:
#                   현재 보고 있는 방이 대실이 가능하다면
                    if rooms[i] <= start_T:
#                       그 방에 현재 예약을 할당하고
                        rooms[i] = end_T
#                       예약 완료 체크
                        booked = True
#           모든 순회가 끝났는데 예약을 못했다면 새로운 방을 만들어주자
            if not booked:
                rooms.append(end_T)
#           방 배정이 끝날때마다 방들의 시간을 다시 정렬해주자
#           정렬을 함으로써 순회를 하면서 제일 효율적으로 방을 예약할 수 있음
            rooms.sort()
            
#   전체 배정된 방의 개수가 정답
    answer = len(rooms)
            
    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))