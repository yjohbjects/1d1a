# 10814_나이순 정렬

def merge_sort(people:list):

    if len(people) > 1:
        mid = len(people)//2

        left = people[:mid]
        right = people[mid:]

        merge_sort(left)
        merge_sort(right)

        l = r = k = 0

        while l != len(left) and r != len(right):
            if left[l][0] <= right[r][0]:
                people[k] = left[l]
                k += 1
                l += 1

            elif left[l][0] > right[r][0]:
                people[k] = right[r]
                k += 1
                r += 1

        while l != len(left):
            people[k] = left[l]
            k += 1
            l += 1

        while r != len(right):
            people[k] = right[r]
            k += 1
            r += 1




N = int(input())

people = []

# 나이는 숫자로 저장
for _ in range(N):
    age, name = input().split()
    people.append([int(age), name])

merge_sort(people)

# join 하려고 했는데 나이가 int라 안됨
# 그래서 f스트링 죠짐
for person in people:
    print(f'{person[0]} {person[1]}')
