import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [float('inf')] * (k+1)
dp[0] = 0
dp[min(coins)] = 1

# k지점에서의 최소 개수
# min(dp[k-coins[0]], dp[k-coins[1]], ...) + 1

for i in range(min(coins)+1, k+1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i-coin] + 1)

# for i in range(k+1):
#         print("dp[{0}]: {1}".format(i, dp[i]))
if dp[k] == float('inf'):
    print(-1)
else:
    print(dp[k])