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
    
        