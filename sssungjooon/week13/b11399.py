# 사람의 수 N
N = int(input())
# 각 사람이 돈을 인출하는 데 걸리는 시간
time = list(map(int,input().split()))

# 애초에 오름차순으로 정렬을 하면 일일히 구할 필요가 없다
# 인덱스와 값을 enumerate 함수를 이용해서 새로운 리스트에 할당한다.
case = []
for idx, t in enumerate(time) :
    case.append([idx, t])

# 두번째를 기준으로 정렬
best_case = sorted(case, key=lambda x:x[1])

time_sum = 0
result = 0

for i in range(N):
    t = best_case[i][1]
    time_sum += t
    result += time_sum

print(result)