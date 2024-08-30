arr = list(map(int, input().split()))

if(arr[0] == arr[1] and arr[0] == arr[2]):
    print(arr[0] * 1000 + 10000)
    exit()

if(arr[0] == arr[1]):
    print(arr[0] * 100 + 1000)
    exit()

if(arr[0] == arr[2]):
    print(arr[0] * 100 + 1000)
    exit()

if(arr[2] == arr[1]):
    print(arr[2] * 100 + 1000)
    exit()

print(max(arr) * 100)