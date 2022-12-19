# B1181_단어 정렬

def merge_sort(words:list):

    if len(words) > 1:
        mid = len(words) // 2

        left = words[:mid]
        right = words[mid:]

        merge_sort(left)
        merge_sort(right)

        l = r = k = 0

        while l != len(left) and r != len(right):

            # 왼쪽 단어가 오른쪽 단어보다 짧다면 words에 넣음
            if len(left[l]) < len(right[r]):
                words[k] = left[l]
                k += 1
                l += 1
            # 오른쪽 단어가 왼쪽 단어보다 짧다면 words에 넣음
            elif len(left[l]) > len(right[r]):
                words[k] = right[r]
                k += 1
                r += 1
            # 왼쪽단어와 오른쪽 단어의 길이가 같다면
            # 둘중 사전상 앞에있는 것을 words에 넣음
            else:
                if left[l] < right[r]:
                    words[k] = left[l]
                    k += 1
                    l += 1
                else:
                    words[k] = right[r]
                    k += 1
                    r += 1

        while l < len(left):
            words[k] = left[l]
            k += 1
            l += 1

        while r < len(right):
            words[k] = right[r]
            k += 1
            r += 1


N = int(input())

words = list(set([input() for _ in range(N)]))


merge_sort(words)


for word in words:
    print(word)