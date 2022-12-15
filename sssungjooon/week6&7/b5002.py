# 정인이는 강남의 유명한 클럽 Top Root의 도어맨이다. 
# 정인이는 항상 클럽에 들어가있는 남자와 여자의 차이를 머리속에 계산하고 있어야 한다. 
# 이 차이가 정인이가 기억할 수 있는 값보다 크게 된다면 남은 사람들은 클럽에 입장을 할 수 없게 된다.
# 줄을 서 있는 순서와 정인이가 기억할 수 있는 차이의 최댓값이 주어졌을 때, 
# 클럽에 있는 사람의 수의 최댓값을 구하는 프로그램을 작성하시오.

# 정인이가 기억할 수 있는 가장 큰 차이
balance = int(input())

# 클럽 입장하는 사람 줄
wait = list(input())

# 클럽 안에 들어가있는 사람 리스트
club = []

# 남녀 세는 카운트
m_count = 0
w_count = 0

## 1등은 남자든 여자든 입장
#club.append(wait[0])
#wait.pop(0)
## 그리고 남자인지 여자인지는 카운트
#if club[0] == 'M' :
#    m_count += 1
#elif club[0] == 'W' :
#    w_count += 1

# 이제부터 입장 판별 시작
#for i in range(len(wait)) :
#    if wait[0] == 'M' :

# 남녀 차이가 메모리(기억하는 차이)보다 작을 때까지만 
while abs(m_count - w_count) <= balance :
    if wait :
        if wait[0] == 'M' and abs(m_count - w_count) < balance :
            club.append(wait.pop(0))
            m_count += 1
        elif wait[0] == 'W' and abs(m_count - w_count) < balance :
            club.append(wait.pop(0))
            w_count += 1
        # 근데 현재 기억하는 차이와 남녀 차가 같다면, 
        # 그 다음 사람 성별 확인 후 먼저 입장
        # 근데 그 다음 사람도 앞사람과 성별이 같다면 종료
        elif wait[0] == 'M' and abs(m_count - w_count) == balance :
            if wait[1] == 'W' :
                club.append(wait.pop(1))
                w_count += 1
            elif wait[1] == 'M' and (m_count - w_count) == balance :
                break
            # 근데 여자가 더 많은데 대기 첫번째가 남자라면 밸런스 맞추기 위해 바로 입장
            elif w_count - m_count == balance :
                club.append(wait.pop(0))
                m_count += 1
        elif wait[0] == 'W' and abs(w_count - m_count) == balance :
            if wait[1] == 'M' :
                club.append(wait.pop(1))
                m_count += 1
            elif wait[1] == 'W' and (w_count - m_count) == balance :
                break
            # 근데 남자가 더 많은데 대기 첫번째가 여자라면 밸런스 맞추기 위해 바로 입장
            elif m_count - w_count == balance :
                club.append(wait.pop(0))
                w_count += 1
    elif not wait :
        break

print(len(club))

# print(wait)
print(wait)
print(club)