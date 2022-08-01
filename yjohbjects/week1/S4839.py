test_case = int(input())
count = 0
while count < test_case:
    p, a, b = map(int, input().split())

    left_a = 1
    right_a = p
    left_b = 1
    right_b = p
    while True:
        center_a = (left_a + right_a)//2
        center_b = (left_b + right_b)//2

        # draw
        if a == center_a and b == center_b:
            print(f'#{count+1} 0')
            break

        # a
        if a == center_a:
            print(f'#{count+1} A')
            break
        elif a > left_a and a < center_a:
            right_a = center_a
        elif a > center_a and a < right_a:
            left_a = center_a

        # b
        if b == center_b:
            print(f'#{count+1} B')
            break
        elif b > left_b and b < center_b:
            right_b = center_b
        elif b > center_b and b < right_b:
            left_b = center_b
    
    count += 1