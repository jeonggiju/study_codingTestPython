import sys

dir = [
    [1,0], #좌
    [0, -1], #하
    [-1,0], #우
    [0,1] # 상
]

def findPath(maze, finIdx):
    moveCount = 1
    backCount = 0
    
    visited = set()
    stack = [[0,0]]

    while stack:
        currentIdx = stack[-1]
        visited.add(tuple(currentIdx)) 
        
        # 목적지에 도달
        if currentIdx == finIdx:
            print("도달 ㅎ")
            break

        moveFlag = False
        # 이동가능할 때
        for dx, dy in dir:
            nextIdx = [currentIdx[0] + dx, currentIdx[1] + dy] 
            if 0 <= nextIdx[0]< len(maze) and 0 <= nextIdx[1] < len(maze[0]) and maze[nextIdx[0]][nextIdx[1]] == '1' and tuple(nextIdx) not in visited :
                stack.append(nextIdx)
                moveCount += 1
                moveFlag = True
                break
        
        if moveFlag == False:
            backCount += 1
            stack.pop()
        
    print(moveCount, backCount)

def main():
    input = sys.stdin.readline
    row, col = map(int, input().split())

    maze = [[] for _ in range(row)]
    for i in range(row):
        maze[i] = input().strip()
    # print(type(maze[2][2]))
    findPath(maze, [row-1, col-1])
    
if __name__ == "__main__":
    main()