import sys

input = sys.stdin.readline
n,m = map(int, input().split())
ls = list(map(int, input().split()))
sumTable = [list(map(int, input().split())) for _ in range(m)]

dp = [[0 for _ in range(n+1)]for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = ls[i-1]

start = 1
for x in range(start, n+1):
    for y in range(start+1,n+1):
        dp[x][y] = dp[x][y-1] + ls[y-1] 
    start += 1
    

for i, j in sumTable:
    print(dp[i][j])