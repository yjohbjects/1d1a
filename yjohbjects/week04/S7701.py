import sys
sys.stdin = open('s_input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    # 세트로 받아서 중복 요소 없게 함 
    names = set(input() for _ in range(N))
    
    # 가나다로 나열
    names = sorted(list(names))
    names = sorted(names, key=len)
    
    # 프린트
    print(f'#{t}')
    print(*names, sep='\n')
