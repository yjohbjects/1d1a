import sys
sys.stdin = open("7701.txt")

# 염라대왕은 이승의 사람들의 모든 이름을 가지고 있다.
# 어느날 저승에 일어난 진도 8.0 지진에 항상 정리되어 있던 이승 명부가 흐트러졌다.
# 이승 명부는 이름의 길이가 짧을수록 이 앞에 있었고, 같은 길이면 사전 순으로 앞에 있었다.
# 이왕 이렇게 된 김에 모든 이름을 다시 정리하고 같은 이름은 하나만 남겨놓기로 한 염라대왕을 도와주자.

T = int(input())

for test_count in range(1,T+1):
    # 이승 명부의 이름 개수 N
    N = int(input())
    # N개의 줄에 걸쳐 알파벳 소문자로 이루어진 이름들 주어짐
    name = []
    for n in range(N) :
        temp = input()
        name.append(temp)
    
    # 세트로 이름 중 중복된 이름 제거 -> 그 후 다시 리스트
    # -> 그 후 sorted로 알파벳순 정렬
    new_name = list(set(name))
    n2_name = sorted(new_name, key=lambda x: (len(x), x))

    # print할 때 # 먼저 출력
    print(f'#{test_count}')

    # 그 후 이름들은 몇 줄에 걸쳐 출력
    for i in n2_name :
        print(i)

