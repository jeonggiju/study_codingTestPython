import sys
from collections import deque

dir = [
    [0, 1],  # 우
    [1, 0],  # 하
    [0, -1],  # 좌
    [-1, 0]  # 상
]

def bfsMazing(maze, finalIdx):
    queue = deque()
    queue.append([0,0])
    
    # 메모리 초과의 주범
    visited = [[0,0]]
    
    while queue:
        currentIdx = queue.popleft()
        
        if finalIdx == currentIdx:
            break
        else:
            for dy, dx in dir:
                nextIdx = [currentIdx[0] + dy, currentIdx[1] + dx]
                if 0 <= nextIdx[0] < len(maze) and 0 <= nextIdx[1] < len(maze[0]) and nextIdx not in visited and maze[nextIdx[0]][nextIdx[1]] >0:
                    maze[nextIdx[0]][nextIdx[1]] = maze[currentIdx[0]][currentIdx[1]] + 1
                    queue.append(nextIdx)

    print(maze[finalIdx[0]][finalIdx[1]])

def main():
    input = sys.stdin.readline
    rows, cols = map(int, input().split())
    maze = [[] for _ in range(rows)]
    
    for i in range(rows):
        str = input().strip()
        for j in range(cols):
            maze[i].append(int(str[j]))
    
    bfsMazing(maze, [rows-1, cols-1])
    
        
if __name__ == "__main__":
    main()