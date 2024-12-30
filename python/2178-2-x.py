import sys

dir = [
    [1,0], #좌
    [0,1], #하
    [-1,0], #우
    [0,-1] #상
]

def mazing(maze, startX, startY, finalX, finalY):

    stack = [[startX, startY]]
    visited = []
    
    while stack:
        currentIdx = stack[-1]
        if [currentIdx[0],currentIdx[1]] not in visited:
            visited.append([currentIdx[0],currentIdx[1]])
        
        if currentIdx[0] == finalX and currentIdx[1] == finalY:
            print(maze[currentIdx[0]][currentIdx[1]])
            break
        
        Flag = False
        for dx, dy in dir:
            nextIdx = [currentIdx[0]+dx, currentIdx[1]+dy]
            if 0 <= nextIdx[0] < len(maze) and 0 <= nextIdx[1] < len(maze[0]) and [nextIdx[0], nextIdx[1]] not in visited and maze[nextIdx[0]][nextIdx[1]] > 0 :
                maze[nextIdx[0]][nextIdx[1]] = maze[currentIdx[0]][currentIdx[1]] + 1  
                stack.append([nextIdx[0], nextIdx[1]])
                Flag = True
                break
        
        if not Flag:
            stack.pop()    
    print("결과는: {}".format(maze[finalX][finalY]))


def main():
    input = sys.stdin.readline
    rows, cols = map(int, input().split())
    
    mazeVisited = [[] for _ in range(rows)]
    for i in range(rows):
        mazeVisited[i] = input().strip()
    
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if mazeVisited[i][j] == '1':
                maze[i][j] = 1
    
    mazing(maze, 0, 0, rows-1, cols-1)
    
if __name__ == "__main__":
    main()