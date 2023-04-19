import copy
import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())

stats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 배열의 길이가 N // 2가 되면 해당시점에서 print 찍어보기
# 배열을 순회하면서 있으면 넘어가고 없으면 추가
# 추가하고 다음 넣고, 빼주기?

possible_start = []

start_list = []

# 인덱스에 따라 스타트팀에 있다면 1로, 없다면 0으로 표시
is_start = [0] * (N + 1)
def make_team(arr):

    # 팀원수가 N의 절반이 되었을 경우
    if sum(arr) == N // 2:
        # 최종 가능한 팀 목록에 해당 경우의수가 없다면 추가
        if arr not in possible_start:
            # 딥카피 안하면 넣을 때마다 배열이 바뀜...
            # 이유아는 사람 설명좀 ㅠ
            # arr: [1, 2] / possible_start: [[1, 2]]
            # arr: [1, 3] / possible_start: [[1, 3], [1, 3]]
            # 최종적으로는 [[], [], []] 이런식으로 출력됨
            arr_copied = copy.deepcopy(arr)
            possible_start.append(arr_copied)
        return

    # 순회하면서 
    for i in range(1, N + 1):
        # print(i)
        # 해당 인원을 아직 포함시키지 않았다면
        if arr[i] == 0:
            arr[i] = 1
            make_team(arr)
            # 해당 인원빼고 다음 단계 진행
            arr[i] = 0

# 가능한 팀 모두 만들어보기
make_team(is_start)



# 팀을 순회하면서 2 P (N // 2)의 순열을 만들어서 해당 좌표값을 더하고
# 1의 순열을 만들어 총합 구하고, 0의 순열을 만들어 총합을 구한 후
# arr: 순열이 들어갈 빈배열
# pool: 순열을 만들 숫자를 뽑는 배열
# stat: 해당팀의 스탯 리스트
def per_for_stat(arr, pool, stat):

    # 두명 생기면
    if len(arr) == 2:
        stat.append(stats[arr[0] - 1][arr[1] - 1])
        return
    
    # 두명 만들기
    for num in pool:
        if num not in arr:
            arr.append(num)
            per_for_stat(arr, pool, stat)
            arr.pop()

# 최대 점수차는 모든 경우의 수에서 100점과 1점을 받는 경우
min_diff = 99 * (N // 2) * (N // 2 - 1)

# abs(1순열, 0순열) 하고 min_diff와 비교
for team in possible_start:
    
    start_team = []
    start_team_stat = []
    link_team = []
    link_team_stat = []

    for i in range(1, N + 1):
        if team[i]:
            start_team.append(i)
        else:
            link_team.append(i)

    per_for_stat([], start_team, start_team_stat)
    per_for_stat([], link_team, link_team_stat)

    min_diff = min(min_diff, abs(sum(start_team_stat) - sum(link_team_stat)))

print(min_diff)