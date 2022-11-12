# B11053_가장 긴 증가하는 부분 수열

def binary(last, arr, x):

    start = 0
    while start < last:
        mid = (last + start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            last = mid
    return last
N = int(input())
A = list(map(int, input().split()))

arr = [A[0]]

last = 0

for now in range(1,N):
    if A[now] > arr[-1]:
        arr.append(A[now])

    else:
        idx = binary(len(arr), arr, A[now])
        arr[idx] = A[now]

print(len(arr))