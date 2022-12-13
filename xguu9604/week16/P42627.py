def solution(jobs):
    answer = 0
    N = len(jobs)
    # 우선 작업의 시작 시간을 기준으로 정렬
    # 여기서 요청 시간이 동일한 경우는 수행 시간대로 정렬을 미리 해주는게 맞음
    jobs.sort(key=lambda x: (x[0], x[1]))
    # 맨 첫 작업부터 계산 시작
    job = jobs.pop(0)
    # 현재까지 진행된 작업이 끝나는 시간
    now_time = job[0] + job[1]
    # 각 작업 요청부터 끝나는데 걸리는 시간의 총합
    total_time = now_time - job[0]
    # 다음 작업으로 와야할 고려 대상들을 담을 리스트
    to_think = []
    # 해야할 작업이 남아있다면 계속 반복
    while jobs:
        # 해야할 작업중에 현재 작업이 끝나는 시간 이전의 시작하는 작업이 있으면
        if jobs[0][0] <= now_time:
            # 그 작업들을 전부 고려대상에 넣어주자
            while jobs[0][0] <= now_time:
                to_think.append(jobs.pop(0))
                if not jobs:
                    break
        # 해야할 작업들이 현재 작업이 끝나는 시간 이후에 시작하면서 고려 대상이 아직 없다면
        elif not to_think:
            # 제일 앞에 작업 친구를 비교해서
            if now_time < jobs[0][0]:
                # 그 친구 시작시간을 우선 현재 시간으로
                now_time = jobs[0][0]
            # 현재 시간과 시작 시간이 같은 친구들 모두 추가
            while jobs[0][0] == now_time:
                to_think.append(jobs.pop(0))
                if not jobs:
                    break
        # 고려 대상을 걸리는 시간을 기준으로 정렬
        to_think.sort(key=lambda x: (x[1], x[0]))
        # 제일 빨리 끝나는 친구를 작업하자
        job = to_think.pop(0)
        # 현재 시간은 그 작업이 끝나는 시간
        now_time += job[1]
        # 총 작업 시간에 현재 시간에서 작업 시작 시간을 뺀값을 더해주자
        total_time += now_time - job[0]
    # 위의 반복을 돌고 아직 덜 마친 작업이 있는 경우 나머지 작업을 전부 처리
    while to_think:
        # 여기도 혹시 몰라서 조건을 추가해서 계산
        to_think.sort(key=lambda x: (x[0], x[1]))
        if to_think[0][0] > now_time:
            now_time = to_think[0][0]
        else:
            to_think.sort(key=lambda x: (x[1], x[0]))
        job = to_think.pop(0)
        now_time += job[1]
        total_time += now_time - job[0]

    answer = total_time // N
    return answer