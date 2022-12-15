# P42627_디스크 컨트롤러

import heapq
# 최소힙 활용

def solution(jobs):
    # 최소힙 만들 리스트
    heap = []

    # job의 시작시간과 남은 소요시간 초기화
    start_time,job_rest_time = 0, 0
    # 각 job의 총 걸린 시간을 더해줄 total
    total = 0
    # 현재 시간을 나타내는 time
    time = 0
    # jobs 리스트의 인덱스
    job_idx = 0
    # jobs를 입력시간 기준으로 오름차순 정렬해준다
    jobs.sort()

    # 루프돌면서 진행
    while True:

        # 아직 힙에 입력되지 않은 job이 남아있고,
        # 현재 남은 job 중 요청시간이 현재시간(time)과 같다면 힙에 넣어줌
        # 요청시간이 동일한 job이 여러개 있을 수 있기 때문에 while로 돌아줌
        # 이걸 놓쳐서 테스트 20 빼고 다 시간초과남 ㄷㄷ
        while job_idx<len(jobs) and jobs[job_idx][0] == time:
            # 최소힙 안에서는 요청시간이 아닌 소요시간 순으로 정렬하기 위해
            # 위치 바꿔서 heappush해줌
            j_start, j_time = jobs[job_idx]
            heapq.heappush(heap, [j_time, j_start])
            # 다음 job 확인을 위해 idx +1
            job_idx += 1

        # 만약 힙에 작업이 남아있고,
        # 현재 작업중인 job이 없다면
        if len(heap)>0 and job_rest_time <= 0:
            # 소요시간이 가장 적은 job을 pop해서 작업 시작
            job_rest_time, start_time = heapq.heappop(heap)

        # 시간이 1초 지남
        time += 1
        # 1초 지났으니 현재 작업중인 job의 남은 소요시간은 -1 됨
        job_rest_time -= 1
        # 만약 현재 작업중인 job의 작업이 끝났다면
        if job_rest_time == 0:
            # total에 [요청부터 종료까지 걸린시간]을 더해줌
            this_job_time = time - start_time
            total += this_job_time
            # jobs에 있는 모든일을 처리했다면
            # while문 종료
            if job_idx == len(jobs) and len(heap) == 0:
                break
    # total을 평균내어 answer에 입력
    answer = total//job_idx

    return answer

