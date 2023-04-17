import sys
sys.stdin = open('in.txt')

N, M = map(int, sys.stdin.readline().split())

paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

tets = [
    # 길쭉이
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    # 뚱뚱이
    [(0, 1), (1, 0), (1, 1)],
    # T
    [(0, 1), (0, 2), (1, 1)],
    [(0, 1), (-1, 1), (0, 2)],
    [(0, 1), (-1, 1), (1, 1)],
    [(1, 0), (2, 0), (1, 1)],
    # 번개
    [(1, 0), (1, 1), (2, 1)],
    [(0, 1), (-1, 1), (-1, 2)],
    # [(-1, 0), (-1, 1), (-2, 1)],
    [(0, 1), (-1, 1), (1, 0)],
    [(0, 1), (1, 1), (1, 2)],
    # 기역1
    [(1, 0), (2, 0), (2, 1)],
    [(1, 0), (0, 1), (0, 2)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (0, 2), (-1, 2)],
    # 기역2
    # [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 0), (2, 0)],
    [(0, 1), (-1, 1), (-2, 1)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (1, 1), (1, 2)]
]

max_val = 0
for i in range(N):
    for j in range(M):

        # 개 복잡한 델타이동
        for tet in tets:
            ni_0, nj_0 = i + tet[0][0], j + tet[0][1]
            ni_1, nj_1 = i + tet[1][0], j + tet[1][1]
            ni_2, nj_2 = i + tet[2][0], j + tet[2][1]

            # 델타이동 결과 내부에 있다면
            if (0 <= ni_0 < N and 0 <= nj_0 < M and
                0 <= ni_1 < N and 0 <= nj_1 < M and
                0 <= ni_2 < N and 0 <= nj_2 < M):
                val = paper[i][j] + paper[ni_0][nj_0] + paper[ni_1][nj_1] + paper[ni_2][nj_2]

                # 최대값 갱신 작업
                max_val = max(val, max_val)
                # print(tet)

print(max_val)