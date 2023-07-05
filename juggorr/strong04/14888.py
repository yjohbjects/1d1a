import sys
sys.stdin = open('in.txt')

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
# 연산자마다 갯수가 들어있는 배열
op_cnts = list(map(int, sys.stdin.readline().split()))
# 연산자 총 갯수
M = sum(op_cnts)
# 연산자 들어갔는지 확인위한 배열
checked = [0] * M
# 모든 연산자의 배열
ops = []
# 연산자 순열결과 배열
ops_for_cal = ['?'] * M
# 연산자 표시 배열
op_list = ['+', '-', '*', '//']
# 이전에 들어갔던 기호 체크
pre_op = '!'

# 0부터 3 까지 op에 넣어주기
for i in range(4):
    # 연산자 갯수에 들어있는 갯수만큼
    for _ in range(op_cnts[i]):
        ops.append(op_list[i])
# print(ops)

# 임의의 최대, 최솟값 정하기
min_result = 1e10
max_result = -1e10

# 결과 계산하는 함수
# arr1은 숫자 배열, arr2는 연산자 배열
def res_cal(arr1, arr2):
    # 리턴할 결과값 정의
    result = arr1[0]
    # 숫자 순회하면서
    for i in range(N - 1):
        # 더하기
        if arr2[i] == '+':
            result += arr1[i + 1]
        # 빼기
        elif arr2[i] == '-':
            result -= arr1[i + 1]
        # 곱하기
        elif arr2[i] == '*':
            result *= arr1[i + 1]
        # 나누기
        else:
            # 음수 일 경우
            if result < 0:
                result = -(-result // arr1[i + 1])
            # 양수 일 경우
            else:
                result = result // arr1[i + 1]
    # 계산 끝나면 결과값 리턴하기
    return result        

def ops_where(cnt, cur_op):
    global min_result, max_result, pre_op

    # 빠졌던 같은 기호가 들어온다면 그즉시 종료
    if pre_op == cur_op:
        return
    
    else:
        pre_op = '!'
        # 모든 연산자를 집어넣었다면
        if cnt == M:
            # 계산 결과값을 내서 갱신하기
            result = res_cal(numbers, ops_for_cal)
            # 최댓값 갱신
            max_result = max(result, max_result)
            # 최솟값 갱신
            min_result = min(result, min_result)
            return
        
        for i in range(M):
            # 해당 기호를 사용한 적이 없다면
            if checked[i] == 0:
                checked[i] = 1
                ops_for_cal[cnt] = ops[i]
                ops_where(cnt + 1, ops[i])
                checked[i] = 0
                ops_for_cal[cnt] = '?'
                pre_op = ops[i]

ops_where(0, '?')
print(max_result)
print(min_result)