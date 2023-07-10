N = int(input())
# i = 0
# N이 3의 몇제곱인지 구하기
# while N > 1:
#     N //= 3
#     i += 1

def print_stars(cnt, stars):
    # print('여긴왔음')

    if cnt == N:
        for star in stars:
            print(star)
        # print('여기서 출력')
        return
    
    else:
        # print('여기도')
        pre_stars = []
        for i in range(3):
            if i == 1:
                for star in stars:
                    pre_stars.append(star + ' ' * cnt + star)

            else:
                for star in stars:
                    pre_stars.append(star * 3)

        # print(pre_stars)
        print_stars(cnt * 3, pre_stars)

print_stars(1, ['*'])