# https://school.programmers.co.kr/learn/courses/30/lessons/42888

# def solution(record):
#     answer = []
#
#     log = {}
#     for rcd in record:
#         msg = rcd.split(' ')
#
#         if msg[0] == 'Enter':
#             answer.append(f'{msg[1]}님이 들어왔습니다.')
#             log[msg[1]] = msg[2]
#
#         elif msg[0] == 'Leave':
#             answer.append(f'{msg[1]}님이 나갔습니다.')
#
#         elif msg[0] == 'Change':
#             log[msg[1]] = msg[2]
#
#     for id in log:
#         # print(log[id])
#         for i in range(len(answer)):
#             if id in answer[i]:
#                 change = answer[i].replace(id, log[id])
#                 answer[i] = change
#
#     return answer

def solution(record):
    answer = []

    db = {}
    log = []
    for rcd in record:
        msg = rcd.split(' ')
        if msg[0] == 'Enter' or msg[0] == 'Change':
            db[msg[1]] = msg[2]

        log.append([msg[0], msg[1]])
    print(db)
    
    for record in log: # [action, id]

        if record[0] == 'Enter':
            answer.append(f'{db[record[1]]}님이 들어왔습니다.')

        elif record[0] == 'Leave':
            answer.append(f'{db[record[1]]}님이 나갔습니다.')

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
