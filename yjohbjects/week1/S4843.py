test_case = int(input())

x = 0
while x < test_case:

    list_len = int(input())
    user_list = list(map(int, input().split()))

    result = []
    while len(user_list) > 1:
    # for i in range(len(user_list)//2):
        # max, min 추출해서 result list에 저장
        min = 1000000
        max = 0
        for num in user_list:
            if num < min:
                min = num
            if num > max:
                max = num
        # max, min 저장
        result.append(max)
        result.append(min)
        # 기존 리스트에 max, min 값 삭제
        user_list.remove(max)
        user_list.remove(min)
    if len(user_list) == 1:
        result.append(user_list[0])

    x += 1
    result = result[0:10]
    print(f'#{x}', *result)