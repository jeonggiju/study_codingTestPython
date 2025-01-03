def find_common_divisors(a,b):
    min_value = min(a,b)
    arr = []
    for i in range(1, min_value+1):
        if a % i == 0 and b % i == 0:
            arr.append(i)
    return max(arr)

num = int(input())
ls = []

for i in range(num):
    a, b = map(int, input().split())
    ls.append(a*b//find_common_divisors(a,b))

for i in range(num):
    print(ls[i])