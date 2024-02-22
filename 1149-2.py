import sys

input = sys.stdin.readline
n = int(input())

colorTable = [list(map(int, input().split())) for _ in range(n)]
dp = [ [0] * 3  for _ in range(n+1)] 

# dp[k][0] dp[k][1] dp[k][2]: k번째에 빨강, 초록, 파랑을 썻을 때 최솟값 저장
 # dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + colorTable[k][0] 
 # dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + colorTable[k][1] 
 # dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + colorTable[k][2] 


dp[1][0] = colorTable[0][0]
dp[1][1] = colorTable[0][1]
dp[1][2] = colorTable[0][2]

for k in range(2, n+1):
    dp[k][0] = min(dp[k-1][1], dp[k-1][2]) + colorTable[k-1][0] 
    dp[k][1] = min(dp[k-1][0], dp[k-1][2]) + colorTable[k-1][1] 
    dp[k][2] = min(dp[k-1][0], dp[k-1][1]) + colorTable[k-1][2] 
    
print(min(dp[k]))