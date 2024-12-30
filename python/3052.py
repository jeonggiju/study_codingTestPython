arr = []

for i in range(10):
    m = int(input())
    n = m % 42
    if(n not in arr):
        arr.append(n)
    

print(len(arr))