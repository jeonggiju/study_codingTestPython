import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for i in range(n)]

dp[0][0] = 1

for sum in range(2*n):
    for row in range(n):
        col = sum - row

        if col < 0:
            break
        if col >= n:
            continue
        #목적지 도달
        if graph[row][col] == 0:
            continue

        distance = graph[row][col]
        
        if row+distance < n:
            dp[row + distance][col] += dp[row][col]
        
        if col+distance < n:
            dp[row][col+distance] += dp[row][col]
    
print(dp[n-1][n-1])
        

