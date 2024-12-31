import sys

n = int(input())

def quick(arr, start, end):
    if start>=end:
        return

    pivot = start
    low = start+1
    high = end

    while low <= high:
        while low <= end and arr[low] <= arr[pivot]:
            low+=1

        while high > start and arr[high] >= arr[pivot]:
            high-=1

        if low > high:
            arr[high], arr[pivot] = arr[pivot], arr[high]
        else:
            arr[low], arr[high] = arr[high], arr[low]

    quick(arr, start, high-1)
    quick(arr, high + 1, end)


ls = []
for i in range(n):
    j = sys.stdin.readline()
    ls.append(int(j))

quick(ls, 0, len(ls)-1)

for i in range(n):
    print(ls[i])