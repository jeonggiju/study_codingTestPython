def sort(a ,startIdx, finIdx):
    
    while startIdx < finIdx:
        a[startIdx], a[finIdx] = a[finIdx], a[startIdx]
        startIdx+=1
        finIdx-=1
        

n, m = list(map(int, input().split()))

arr = []

for i in range(1,n+1):
    arr.append(i)

for _ in range(m):
    s, f = list(map(int, input().split()))
    sort(arr, s-1, f-1)
    

for i in range(n):
    print(arr[i])
