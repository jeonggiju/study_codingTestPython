import sys
from collections import deque

dir = [
    (0,1), #좌
    (1,0), #하
    (0,-1), #우
    (-1,0) #상
]

def bfsMazing(maze, finalIdx):
    queue = deque()
    queue.append((0,0))
    
    while queue:
        y, x = queue.popleft()
        for dy, dx in dir:
            if 0<=dy+y<len(maze) and 0 <= dx+x < len(maze[0]):
                if maze[y+dy][x+dx] == 1: # 처음 방문했을 경우
                    maze[y+dy][x+dx] = maze[y][x] +1
                    queue.append((y+dy, x+dx))
                    
    print(maze[finalIdx[0]][finalIdx[1]])

def main():
    input = sys.stdin.readline
    rows, cols = map(int, input().split())
    maze = []
    
    for i in range(rows):
        # map(function, iterable)
        # map는 iterable 각 요소에 function을 적용하여 반환 -> iterable형태로 반환
        maze.append(list(map(int,input().strip())))  # 문자열을 입력받기에 각 한글자한글자를 int형으로 반환
        
    bfsMazing(maze, [rows-1, cols-1])
        
if __name__ == "__main__":
    main()