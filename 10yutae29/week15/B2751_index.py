# B2751_수 정렬하기2

def merge_sort(numbers):

    # 리스트에 숫자가 1개가 아니라면 분할 해줘야함
    if len(numbers) > 1:

        # 중간값을 기준으로 left right로 나눠줌
        mid = len(numbers) // 2

        left = numbers[:mid]
        right = numbers[mid:]

        # 리스트에 1개의 숫자만 들어갈때까지 나눠줌
        merge_sort(left)
        merge_sort(right)

        # 왼쪽리스트 오른쪽리스트의 숫자를 비교하기 위한 인덱스
        l = 0
        r = 0
        # 왼쪽리스트 오른쪽리스트의 숫자를 비교하여 더 작은 숫자를 정하고
        # 그 숫자가 들어갈 numbers리스트의 위치
        k = 0

        # 왼쪽 리스트의 숫자와 오른쪽 리스트의 숫자가 아직 numbers에 들어가지 않았다면
        while l != len(left) and r != len(right):
            # 왼쪽 리스트의 숫자가 오른쪽 리스트의 숫자보다 작다면
            # 이를 numbers의 k위치에 넣고
            # 왼쪽 리스트의 다음숫자를 파악하기 위해 l + 1 해준다
            if left[l] < right[r]:
                numbers[k] = left[l]
                l += 1
            # 오른쪽 리스트의 숫자가 왼쪽 리스트의 숫자보다 작다면
            # 이를 numbers의 k위치에 넣고
            # 오른쪽 리스트의 다음숫자를 파악하기 위해 r + 1 해준다
            else:
                numbers[k] = right[r]
                r += 1
            # numbers에 숫자를 넣어야할 위치를 다음으로 옮겨준다
            k += 1

        # 만약 오른쪽 리스트의 숫자는 numbers에 다 들어가고
        # 왼쪽 리스트의 숫자가 남아있다면
        # 이를 전부 numbers에 다 넣어줌
        while l < len(left):
            numbers[k] = left[l]
            l += 1
            k += 1

        # 만약 왼쪽 리스트의 숫자는 numbers에 다 들어가고
        # 오른쪽 리스트의 숫자가 남아있다면
        # 이를 전부 numbers에 다 넣어줌
        while r < len(right):
            numbers[k] = right[r]
            r += 1
            k += 1


N = int(input())

numbers = [int(input()) for _ in range(N)]

merge_sort(numbers)

for i in numbers:
    print(i)