# S4869 종이붙이기

import sys
sys.stdin = open('S4869_input.txt')

test_case = int(input())

z = 0
while z < test_case:
    x = int(input())

    result = [1, 3]
    for i in range(2, x//10):
        result.append(result[i-2] + 2**i)
        # print(result)

    z+= 1
    print(f'#{z} {result[-1]}')