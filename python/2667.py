import sys
from collections import deque

def bfs(graph, startY, startX):
    visitedCount = 0
    queue = deque()
    queue.append((startY,startX))
    graph[startY][startX] = 0

    dir = [[-1,0],[1,0],[0,1],[0,-1]]
    
    while queue:
        y, x = queue.popleft()
        visitedCount += 1

        for dy, dx in dir:
            if 0 <= dy+y < len(graph) and 0 <= dx + x < len(graph) and graph[dy+y][dx+x] != 0:
                graph[dy+y][dx+x] = 0
                queue.append((dy+y, dx+x))
                
    return visitedCount

def main():
    input = sys.stdin.readline
    n = int(input().strip()) 
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().strip())))

    record = []
    
    for y in range(n):
        for x in range(n):
            if graph[y][x] != 0 :
                record.append(bfs(graph,y,x))
    record.sort()
    
    print(len(record))
    for i in range(len(record)):
        print(record[i])
    
if __name__ == "__main__":
    main()
    



# 현교형 id풀이

# import sys

# def dfs(x, y, id):
#     ids[x][y] = id
#     complexes[id] += 1

#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and ids[nx][ny] < 0:
#             dfs(nx, ny, id)

# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     board = [[int(ch) for ch in sys.stdin.readline().strip()] for _ in range(n)]

#     ids = [[-1] * n for _ in range(n)]
#     directions = [(0, -1), (0, 1), (-1, 0), (1,ㅌ`` 0)]
#     complexes = [] 
#     count = 0
    
#     for i in range(n * n):
#         x, y = i // n, i % n
#         if board[x][y] == 1 and ids[x][y] < 0:
#             complexes.append(0)  # Initialize new complex size
#             dfs(x, y, count)
#             count += 1

#     print(count)
#     for size in sorted(complexes):
#         print(size)