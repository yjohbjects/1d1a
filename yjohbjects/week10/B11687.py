# B11687 팩토리얼 0의 개수

def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

M = int(input()) # (1 ≤ M ≤ 100,000,000)


