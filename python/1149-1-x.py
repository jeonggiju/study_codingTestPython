import sys

input = sys.stdin.readline
n = int(input())

colorTable = [list(map(int, input().split())) for _ in range(n)]

# n*2: 한칸은 최소값, 한칸은 선택된 인덱스값
dp = [ [0] * 2  for _ in range(n+1)] 
dp[1][0] = min(colorTable[0])
dp[1][1] = colorTable[0].index(dp[1][0])

#dp[k] = dp[k-1] + colorTable[k][l] (l은 앞의 k-1에서 택되지 않은 것)


for i in range(2, n+1):
    dp[i][0] = dp[i-1][0]
    beforeIdx = dp[i-1][1]
    minValue = 1000
    for currentIdx in range(3):
        if currentIdx == beforeIdx:
            continue
        
        if minValue > colorTable[i-1][currentIdx]:
            minValue = colorTable[i-1][currentIdx]
            dp[i][1] = currentIdx
            
    dp[i][0] += minValue
    
print(dp)