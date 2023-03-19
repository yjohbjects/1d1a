# P150365_미로 탈출 명려어 REAL

def solution(n, m, x, y, r, c, k):
    answer=''

    # 하 좌 우 상
    # 문제에서 가로축이 y 세로축이 x임

    # 출발지점에서 탈출지점 까지의 가로 세로 거리
    sero_diff = r-x
    garo_diff = c-y

    # 총거리와 k 모두 짝수이거나 홀수가 아니라면 불가능
    if k%2 != (abs(sero_diff)+abs(garo_diff))%2 or k<(abs(sero_diff)+abs(garo_diff)):
        return 'impossible'

    # (n,1) 왼쪽 맨 아래 지점까지 먼저 갈거임임
    # d와 l이 사전순으로 빠르기 때문1
    # 먼저 dddddd 를 채우고 그다음 lllll 을 채우고 시작할거임
    sero_to_n1 = n - x
    garo_to_n1 = abs(1 - y)
    answer += sero_to_n1*'d' +garo_to_n1*'l'

    # (n,1) 부터 탈출지점까지 가로 세로 거리
    sero_n1_to_end = abs(r - n)
    garo_n1_to_end = c - 1

    # now = 출발지점 -> (n,1) 까지의거리 + (n,1) -> 탈출지점 까지의 거리
    now = sero_to_n1 + garo_to_n1 + sero_n1_to_end + garo_n1_to_end

    # 만약 현재 이동한것 보다 더 이동해야한다면
    # rl이 ud보다 사전순으로 빠르기 때문에 rl을 answer에 채워줌
    while now < k:
        answer += 'rl'
        now += 2

    # 만약 현재 이동한것보다 적게 이동해야한다면
    while now > k:
        # 출발지에서 (n,1)까지 이동하는 경로중 마지막 동작이 l(왼쪽으로 이동) 이라면
        # l을 제외하고 이에 맞추기 위해 (n,1)부터 탈출지점까지 가는 r(오른쪽으로 이동)의 횟수도 하나 제외
        if answer[-1] == 'l':
            answer=answer[:-1]
            garo_n1_to_end -= 1
            now -=2
        # 마지막 동작이 d(아래로 이동)이라면
        # d 를 제외하고 이에 맞추기 위해 (n,1)부터 탈출지점까지 가는 u(위쪽으로 이동)의 횟수도 하나 제외
        else:
            answer = answer[:-1]
            sero_n1_to_end -= 1
            now -= 2

    # 이동횟수와 k를 맞췄으면
    # 탈출지점까지 이동하는 r과 u를 answer에 더해줌
    answer += garo_n1_to_end*'r' + sero_n1_to_end*'u'



    return answer

print(solution(3,4,2,3,3,1,5))
print(solution(2,2,1,1,2,2,2))
print(solution(3,3,1,2,3,3,4))