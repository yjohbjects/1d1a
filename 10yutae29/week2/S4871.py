# S4871 그래프 경로

T = int(input()) # 테스트 케이스 개수

for t in range(T):
    ve = list(map(int,input().split()))
    v = ve[0]
    e = ve[1]
    line_infs = []
    for es in range(e):
        line_inf = list(map(int,input().split()))
        line_infs.append(line_inf)
    sg = list(map(int,input().split()))
    s = sg[0]
    g = sg[1]