import sys

input = sys.stdin.readline
n = int(input())

# 입력된 계단의 점수
stairs = [0] * (1+n)

# k번쨰 계단에 도달할 때의 최대값들을 저장
dp = [0] * (1+n)
for i in range(1,n+1):
    stairs[i] = int(input())

# n이 1일 경우
if n == 1:
    print(stairs[1])
    exit(0)

dp[1] = stairs[1]
dp[2] = stairs[1]+stairs[2]

for k in range(3, n+1):
    dp[k] = max(dp[k-2] + stairs[k], dp[k-3] + stairs[k-1] + stairs[k])
print(dp[n])

# 현재 계단 k
# 2가지 경우 
# 1. k-3, k-1, k
# 2. k-2, k

