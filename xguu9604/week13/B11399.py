'''
순서가 빠르면 빠를수록 기다리는 시간에 자주 더해짐
따라서 작은값부터 시간을 나열해서 더해주면 최솟값이 등장
'''


N = int(input())
# 사람들이 걸리는 시간을 리스트로 받아주고
people = list(map(int, input().split()))
# 오름 차순 정렬을 해준다
people = sorted(people)
# 각 사람별로 기다린 시간을 받아줄 리스트를 만들고
times = [0] * N
# 총 걸린 시간을 다 더해줄 변수 선언
answer = 0
# 전체 반복을 돌면서
for i in range(N):
    # 맨 앞사람 시간은 그냥 바로 기록하고
    if i == 0:
        times[i] += people[i]
    # 나머지 사람들은 앞사람이 걸린 시간에 내가 소요한 시간값을 더해준다
    else:
        times[i] = times[i-1] + people[i]
    # 정답에 이번 사람이 기다린 시간을 더해준다
    answer += times[i]
print(answer)