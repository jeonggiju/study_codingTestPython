import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for i in range(n)]

def recur(x,y):
    global count
    distance = graph[x][y]

    if x == n-1 and y == n-1:
        dp[x][y] += 1
        return

    # 오른쪽
    if x + distance < n:
        dp[x + distance][y] += 1
        recur(x + distance, y)

    # 아래
    if y + distance < n:
        dp[x][y + distance] += 1
        recur(x, y + distance)

recur(0,0)
print(dp)
print(dp[n-1][n-1])
