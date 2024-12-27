
def primeNum(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))

c = 0

for i in range(n):
    if primeNum(nums[i]):
        c += 1

print(c)