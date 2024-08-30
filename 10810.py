n, m = map(int, input().split())

arr = [0] * n
 
for _ in range(m):
    
    i, j, k = map(int,input().split())
    
    for a in range(i, i +j-i+1):
        arr[a-1] = k

for i in range(n):
    print(arr[i])