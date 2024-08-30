import math

n = int(input())
arr = list(map(int, input().split()))

m = max(arr) 

for i in range(0, len(arr)):
    arr[i] = arr[i]/m * 100


print(sum(arr)/len(arr))