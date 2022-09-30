import sys
sys.stdin = open('input_B5525.txt')

'''
50점
'''

def counting_ioi(idx, lst):
    is_ioi = 1
    if idx + (2*N + 1) > S:
        return 0
    else:
        for j in range(2*N+1):
            if j % 2 and lst[idx + j] == 'O':
                pass
            elif j % 2 == 0 and lst[idx + j] == 'I':
                pass
            else:
                is_ioi = 0
            if not is_ioi:
                return is_ioi
    return is_ioi

N = int(input())
S = int(input())
ioi = list(map(str, input()))
num_ioi = 0
for i in range(S):
    if ioi[i] == 'I':
        num_ioi += counting_ioi(i, ioi)
print(num_ioi)