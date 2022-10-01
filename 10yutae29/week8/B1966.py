# B1966_프린터 큐
T = int(input())

for t in range(T):
    N, M = map(int,input().split())
    nu = list(map(int,input().split()))
    nums = []
    for idx, n in enumerate(nu):
        nums.append([n, idx])
    p_count = 0
    while True:
        paper = nums.pop(0)
        for num in nums:
            if num[0]>paper[0]:
                nums.append(paper)
                break
        else:
            p_count += 1
            if paper[1] == M:
                break
    print(p_count)

