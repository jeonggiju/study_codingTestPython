import sys

n, m = list(map(int,sys.stdin.readline().split()))

arr = []

for i in range(1,n+1):
    arr.append(i)
    
for i in range(m):
    a, b = list(map(int,sys.stdin.readline().split()))
    arr[a-1], arr[b-1] = arr[b-1], arr[a-1]

for i in range(n):
    print(arr[i])
