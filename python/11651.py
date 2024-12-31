import sys

num = int(sys.stdin.readline())

arr = []

for i in range(num):
    arr.append(list(map(int, sys.stdin.readline().split())))

def merge(arr, left,right):
    i, j, k = 0, 0, 0
    leftSize, rightSize = len(left), len(right)

    while i < leftSize and j < rightSize:
        if left[i][1] < right[j][1]:
            arr[k] = left[i]
            k += 1
            i += 1
        elif left[i][1] > right[j][1]:
            arr[k] = right[j]
            k += 1
            j += 1
        else:
            if left[i][0] <= right[j][0]:
                arr[k] = left[i]
                k += 1
                i += 1
            else:
                arr[k] = right[j]
                k += 1
                j += 1

    while i < leftSize:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < rightSize:
        arr[k] = right[j]
        k += 1
        j += 1

def mergeSort(arr):
    n = len(arr)

    if n < 2:
        return

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    merge(arr, left, right)

mergeSort(arr)

for i in range(num):
    print(arr[i][0], arr[i][1])





