import sys


input = sys.stdin.readline
n = int(input())
dp = [0] * (n+1)
ls = [0] * (n+1)
ls[1] = 0

for k in range(2, n+1):
    dp[k] = dp[k-1] + 1
    ls[k] = k-1
    if k%2 == 0 and dp[k//2] + 1 < dp[k]:
        dp[k] = dp[k//2] + 1
        ls[k] = k//2
    if k%3 == 0 and dp[k//3] + 1 < dp[k]:
        dp[k] = dp[k//3] + 1
        ls[k] = k//3
        

print(dp[n])
idx = n
while idx!= 0:
    print(idx, end=" ")
    idx = ls[idx]
    