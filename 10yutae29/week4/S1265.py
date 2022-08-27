# S1265 달란트

def mul(n_list):    # 리스트 요소 전부 곱하는 함수
    ans = 1
    for n in n_list:
        ans *= n
    return ans

def suum(n_list):   # 리스트 요소 전부 더하는 함수
    ans = 0
    for n in n_list:
        ans += n
    return ans

T = int(input())

for t in range(1, T+1):
    dal, num = map(int, input().split())
    a = dal//num
    a_list = [a]*num
    change_idx = 0
    while suum(a_list) != dal:
        a_list[change_idx] += 1
        change_idx += 1
    print(f'#{t} {mul(a_list)}')







# T = int(input())
# for tc in range(T):
#     N,P = map(int, input().split())
#     print(f"#{tc+1} {(N//P)**(P-N%P)*((N//P)+1)**(N%P)}")