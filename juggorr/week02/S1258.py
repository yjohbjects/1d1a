import sys
sys.stdin = open('S1258.txt')

def bubble_sort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

T = int(input())
for tc in range(T):
    n = int(input())
    stor = [list(map(int,input().split())) for _ in range(n)]
# 값 저장을 위한 dic만들기 key = width, value = height
    dic = {}    
    
    for r in range(n):
        count = 0
        for c in range(n):
            if stor[r][c] > 0:
                count += 1
            elif stor[r][c] == 0 and count != 0:
                dic[count] = dic.get(count, 0) + 1
                count = 0
        
        if count > 0:
            dic[count] = dic.get(count,0)+1

# 약품 정보를 저장하기 위한 리스트 만들기
    chem = []
    for width, height in dic.items():
        chem.append([height * width, height, width])

    bubble_sort(chem)

    res_int = []
    for i in range(len(chem)):
        res_int.append(chem[i][1])
        res_int.append(chem[i][2])

    res_str = map(str, res_int)
    res = ' '.join(res_str)

    print(f'#{tc + 1} {len(chem)} {res}')