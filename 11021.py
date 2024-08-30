import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    a, b= list(map(int, sys.stdin.readline().split()))
    arr.append("Case #{}: {} + {} = {}".format(i+1,a,b,a+b))

for i in range(n):
    print(arr[i])