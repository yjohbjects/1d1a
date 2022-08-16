import sys
sys.stdin = open('sample_input.txt')

# S5097 회전

T = int(input())
for z in range(T):
    N, M = map(int, input().split())
    nums = list(input().split())

    # 맨 앞에껄 맨 뒤로 붙여넣기를 M회 반복
    for i in range(M):
        nums.append(nums.pop(0))

    print(f'#{z+1} {nums[0]}')
