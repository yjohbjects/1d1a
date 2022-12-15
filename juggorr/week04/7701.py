T = int(input())
for tc in range(T):
    N = int(input())
    names = [input() for _ in range(N)]
# 중복 값 제거
    names = list(set(names))
# 길이 순으로 정렬하기
    result = sorted(names, key = lambda x: (len(x), x))
    print(f'#{tc + 1}')
    for i in result:
        print(i)