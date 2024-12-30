import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for k in range(2,n+1):
    dp[k] = dp[k-1] + dp[k-2]
    
result = dp[n] % 10007

print(result)