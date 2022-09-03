# B2839 설탕 배달

# 완전 탐색
# 5x + 3y = n 인지 아닌지
# input/output 테스트 케이스를 해결하려고 하지말고, 문제의 본질을 생각해서 해결하려고 해봐라!!라고 일깨워주는 좋은 문제


n = int(input())
cnt = 99999

for i in range(n//5 + 1):
    for j in range(n//3 + 1):
        if (5 * i) + (3 * j) == n:
            temp = i + j

            if temp < cnt:
                cnt = temp

print(cnt if cnt != 99999 else -1)
