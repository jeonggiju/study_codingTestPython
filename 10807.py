import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())
c = 0

for i in range(n):
    if(arr[i] == t):
        c+=1
print(c)