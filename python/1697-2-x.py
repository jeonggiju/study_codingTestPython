import sys
from collections import deque

        
def dfs(startPoint, findPoint, depth):
    print(startPoint)
    if depth > 1:
        return
    
    if startPoint == findPoint:
        print(depth)
        sys.exit()
    else:
        dfs(startPoint-1, findPoint, depth+1)
        dfs(startPoint*2, findPoint, depth+1)
        dfs(startPoint+1, findPoint, depth+1)
        
def main():
    input = sys.stdin.readline
    startPoint, findPoint = map(int, input().split())
    # print(bfs(startPoint, findPoint))
    dfs(startPoint, findPoint, 0)
    
if __name__ == "__main__":
    main()