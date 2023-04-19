from itertools import permutations, combinations
import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
stats = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

members = [i for i in range(N)]
# print(members)

# 스타트팀은 그냥 반갈죽시키면댐
start_teams = list(combinations(members, N // 2))
# 링크팀은 어떻게 해야 효과적으로 찾을 수 있음?
# print(start_teams)

min_diff = 99 * (N // 2) * (N // 2 - 1)
for start_team in start_teams:

    link_team = []
    # 링크팀을 여기서 만들어볼까
    for i in range(N):
        if i not in start_team:
            link_team.append(i)


    start_stat = 0
    link_stat = 0

    start_stat_coors = list(permutations(start_team, 2))
    link_stat_coors = list(permutations(link_team, 2))

    for coor in start_stat_coors:
        start_stat += stats[coor[0]][coor[1]]

    for coor in link_stat_coors:
        link_stat += stats[coor[0]][coor[1]]

    min_diff = min(min_diff, abs(start_stat - link_stat))

print(min_diff)