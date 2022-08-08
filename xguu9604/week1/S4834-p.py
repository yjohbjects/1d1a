T = int(input())
cnt = 1

while T > 0:
    N = int(input())
    chars = input()
    max_time = 0
    max_comp = ''
    for char in chars:
        if chars.count(char) > max_time:
            max_time = chars.count(char)
            max_comp = char
        elif chars.count(char) == max_time:
            if int(max_comp) < int(char):
                max_comp = char

    print(f'#{cnt} {max_comp} {max_time}')
    cnt += 1
    T -= 1