import sys

input = sys.stdin.readline
lenArr = int(input())
nums = list(map(int, input().split()))

dpArr = [1] * lenArr

for i in range(1, lenArr):
    for j in range(0, i):
        if nums[j] > nums[i]:
            dpArr[i] = max(dpArr[i], dpArr[j] + 1)

print(max(dpArr))
