def solution(n, m, section):
    answer = 0
#     현재 롤러가 페인트를 칠하는 벽의 위치
    paint_spot = 0
#     현재 찍힌 점에서부터 롤러가 칠하는 공간은 1개를 빼줘야 계산이 가능
    m -= 1
#     페인트를 칠해야하는 벽들을 순회하자
    for to_paint in section:
#         첫번째 벽이면 우선 칠하고 보자
        if paint_spot == 0:
#         롤러가 현재 칠하는 곳은 시작점에서부터 롤러 크기까지는 전부 칠하는중
#         그 값보다 적은 벽의 숫자들은 다 칠해지니 시작점이 아닌 끝점을 기록하자
            paint_spot = to_paint + m
            answer += 1
#         나머지 벽의 경우는 조건 찾기
        else:
#         현재 칠해야 하는 지점이 롤러 끝이하면 이미 칠해져있으니 패스
            if to_paint <= paint_spot:
                pass
#         롤러의 범위를 벗어 났다면 여기부터 다시 칠하고 카운팅해주기
            else:
                paint_spot = to_paint + m
                answer += 1
    return answer

print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))