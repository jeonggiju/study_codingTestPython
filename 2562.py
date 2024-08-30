
arr =[]

for i in range(9):
    arr.append(int(input()))

l = 0
max = arr[0]

for i in range(9):
    if(max < arr[i]):
        max = arr[i]
        l = i
print(max, l+1)