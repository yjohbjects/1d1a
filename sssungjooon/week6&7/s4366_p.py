import sys
sys.stdin = open("s4366.txt")

T = int(input())

for test_count in range(1, T+1):
    # 2진수, 3진수 각자 담자
    num2 = list(map(int,input()))
    num3 = list(map(int,input()))

    list_two = []
    list_three = []
    
    sum2 = 0
    sum3 = 0
    result = 0
    
    # 2진수일 때 한자리씩 바꿨을 때의 값을 담자
    # 그전에 잘못 기억한 2진수의 합을 구하자
    for n2 in range(len(num2)):
        sum2 += 2**(len(num2)-n2-1)*num2[n2]

    # 잘못 기억한 3진수의 합을 구하자
    for n3 in range(len(num3)):
        sum3 += 3**(len(num3)-n3-1)*num3[n3]

    # 2진수부터
    for n2 in range(len(num2)):
        # 2진수의 n2번째가 1이라면 0 처리해서 합에서 뺀 값을 리스트에 넣고
        if num2[n2] == 1 :
            temp2 = sum2 - 2**(len(num2)-n2-1)
            list_two.append(temp2)

        # 2진수의 n2번째가 0이라면 해당 자릿수의 숫자를 합에 더한 값을 리스트에 넣는다.
        elif num2[n2] == 0 :
            temp2 = sum2 + 2**(len(num2)-n2-1)
            list_two.append(temp2)

    # 3진수도 진행 (다만 0,1,2 3가지 경우를 구해야한다)
    for n3 in range(len(num3)):
        if num3[n3] == 2 :
            temp3_1 = sum3 - 3**(len(num3)-n3-1)
            temp3_0 = sum3 - (3**(len(num3)-n3-1))*2
            list_three.append(temp3_1)
            list_three.append(temp3_0)
        
        elif num3[n3] == 1 :
            temp3_2 = sum3 + 3**(len(num3)-n3-1)
            temp3_0 = sum3 - 3**(len(num3)-n3-1)
            list_three.append(temp3_2)
            list_three.append(temp3_0)

        elif num3[n3] == 0 :
            temp3_2 = sum3 + (3**(len(num3)-n3-1))*2
            temp3_1 = sum3 + 3**(len(num3)-n3-1)
            list_three.append(temp3_2)
            list_three.append(temp3_1)

    # 2진수, 3진수 각자 한자리씩 다른 합을 넣은 리스트 중 비교하여 같은 숫자가 있다면 출력한다.
    for l2 in list_two :
        for l3 in list_three :
            if l2 == l3 :
                result = l2

    print(f'#{test_count} {result}')
