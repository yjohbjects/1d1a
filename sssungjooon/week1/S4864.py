# 두 개의 문자열 str1과 str2가 주어진다. 
# 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
# 예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 
# 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.

# 첫 줄에 테스트 케이스 개수 T (1 <= T <= 50)
T = int(input())

for test_num in range(1, T+1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    # result의 기본값을 0으로 두고
    result = 0
    for i in range(M-N+1):          # 첫번째부터 M-N+1(마지막 반복 시작점)까지 반복
        if str2[i:i+N] == str1:     # str2 안의 i번째부터 str1의 글자길이만큼 잘랐을 때
            result = 1              # str1이 있다면 result 1을 반환
    
    print('#%d %d' %(test_num, result))