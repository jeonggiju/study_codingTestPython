import sys


input = sys.stdin.readline

n = int(input())

nums = [0] * n
for i in range(n):
    nums[i] = int(input())

maxValue = max(nums)
dp = [0] * (maxValue+1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,maxValue+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]


for i in range(n):
    print(dp[nums[i]])

# 1

# 1 1
# 2

# 1 1 1
# 1 2
# 2 1
# 3

# 1 1 1 1 one
# 1 1 2 two
# 1 2 1 one
# 2 1 1 one
# 2 2 two
# 1 3 three
# 3 1 one
