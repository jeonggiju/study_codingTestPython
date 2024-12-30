n = int(input())

arr = []

for i in range(n):
    m, s = input().split()
    m = int(m)
    s = str(s)
    r = ""
    for j in range(len(s)):
        r += s[j]*m
    arr.append(r)
    
for i in range(len(arr)):
    print(arr[i])