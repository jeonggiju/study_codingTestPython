def primeNum(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
m = int(input())

lst = []
for i in range(n,m+1):
    if primeNum(i):
        lst.append(i)


if len(lst) == 0:
    print(-1)
    exit(0)

print(sum(lst))
print(min(lst))