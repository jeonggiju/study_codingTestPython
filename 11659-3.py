import sys

input = sys.stdin.readline
n,m = map(int, input().split())
ls = list(map(int, input().split()))
sumTable = [list(map(int, input().split())) for _ in range(m)]

dp = [0] *(n+1)
dp[1] = ls[0]

for k in range(2, n+1):
    dp[k] = dp[k-1] + ls[k-1]

for i, j in sumTable:
    print(dp[j] - dp[i-1])
    