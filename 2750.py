num = int(input())
lst = []

for i in range(num):
    lst.append(int(input()))

for i in range(num):
    for j in range(num-i-1):
        if lst[j+1] < lst[j]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

for i in range(len(lst)):
    print(lst[i])