test_case = int(input())

x = 0
while x < test_case:
    word = input()
    include_word = input()
    if word in include_word:
        print(f'#{x+1} 1')
    else:
        print(f'#{x+1} 0')
    x += 1