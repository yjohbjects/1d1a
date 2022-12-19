# B2751_수 정렬하기2

def merge(left:list, right:list):
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result

def merge_sort(numbers:list):
    if len(numbers) == 1:
        return numbers

    left = []
    right = []
    middle = len(numbers) //2

    for n in range(0, middle):
        left.append(numbers[n])
    for n in range(middle, len(numbers)):
        right.append(numbers[n])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

N = int(input())

numbers = [int(input()) for _ in range(N)]

# print(numbers)

print(merge_sort(numbers))