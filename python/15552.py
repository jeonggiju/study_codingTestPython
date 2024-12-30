import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    a, b= list(map(int, sys.stdin.readline().split()))
    arr.append(a+b)
    
for i in range(n):
    print(arr[i])