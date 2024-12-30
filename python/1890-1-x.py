import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for i in range(n)]
queue = deque()
queue.append([0,0])

while queue:
    currentX, currentY = queue.popleft()
    distance = graph[currentX][currentY]
    if distance == 0:
        continue
    # 오른쪽
    if currentX + distance < n:
        dp[currentX+distance][currentY] += 1
        queue.append([currentX+distance, currentY])

    # 아래
    if currentY + distance < n:
        dp[currentX][currentY + distance] += 1
        queue.append([currentX, currentY+distance])

print(dp)
print(dp[n-1][n-1])