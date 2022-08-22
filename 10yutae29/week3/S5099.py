# S5099 피자 굽기

T = int(input())

for t in range(T):
    nm = list(map(int, input().split()))
    hd_size = nm[0]  # 화덕 크기
    pz_num = nm[1]  # 피자 개수
    cheese_nidx = list(map(int, input().split()))  # 치즈양만 있고 피자의 번호는 없는 리스트
    cheese = []
    for num in range(pz_num):  # 피자의 번호와 치즈의 양이 같이 있는 리스트 만들기
        cheese.append([num + 1, cheese_nidx[num]])  # ex) cheese = [[1, 7], [2, 2], [3, 6], [4, 5], [5, 3]]

    hd = [0]*hd_size  # 화덕 셋팅!
    kan_count = 0  # 화덕이 한칸 움직임을 계산 0일 때 1번칸
    andle_idx = hd_size  # 화덕에 안들어간 피자중 첫번째 피자 인덱스
                         # 1번의 경우 화덕에 3개의 피자가 들어가므로 그 다음인 4번째(리스트 인덱스로 3)가 들어간다.

    for one_hd in range(hd_size):  # 화덕에 일단 피자를 다 넣음
        hd[one_hd] = cheese[one_hd]
        kan_count += 1  # 피자를 넣고 화덕이 한칸씩 움직임

    while True:
        hd_idx = kan_count % hd_size  # 칸 움직임 수를 화덕 크기로 나눈 나머지가 확인할 수 있는 화덕의 인덱스
        hd[hd_idx][1] = hd[hd_idx][1] // 2  # 한바퀴 돌면 치즈의 양이 1/2로 줄어듦

        if andle_idx < pz_num and hd[hd_idx][1] == 0:
            # 만약 안들어간 피자가 있고, 현재 확인할 수 있는 피자의 치즈양이 0이라면
            hd[hd_idx] = cheese[andle_idx]  # 기존의 피자를 꺼내고, 아직 안들어간 피자를 넣음
            andle_idx += 1  # 그리고 아직 안들어간 피자의 인덱스를 구함

        nzero_count = 0  # 치즈양이 0이 아닌걸 세는 변수
        for pizza in range(hd_size):
            if hd[pizza][1] != 0:  # 피자의 치즈양이 0이 아니라면
                nzero_count += 1  # +1
                answer = hd[pizza][0]  # answer에 치즈양이 0이 아닌 피자의 번호를 입력
        if nzero_count == 1:  # 만약 화덕에 있는 피자 중 치즈양이 0이 아닌 피자가 1개라면 반복을 끝낸다
            break

        kan_count += 1  # 화덕 한칸 이동 (한바퀴가 아니라 한칸)

    print(f'#{t+1} {answer}')