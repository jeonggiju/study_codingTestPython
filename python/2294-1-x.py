import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[min(coins)] = 1

for i in range(min(coins)+1,k+1):
    minValue = 100000
    for coin in coins:
        if i >= coin and minValue > dp[i-coin]:
            minValue = dp[i-coin]
    dp[i] = minValue + 1


print(dp[k])

# for i in range(k+1):
#     print("dp[{0}]: {1}".format(i, dp[i]))