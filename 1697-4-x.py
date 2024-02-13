import sys
from collections import deque

def bfs(startPoint, findPoint):
    queue = deque()
    queue.append([startPoint, 0])
    maxNum = 1000001
    visited = set()

    while True:
        current = queue.popleft()
        visited.add(current[0])

        if current[0] == findPoint:
            print(current[1])
            return
        else:
            for j in [current[0]*2, current[0]-1, current[0]+1]:
                if j <= maxNum and j not in visited:
                    queue.append([j, current[1]+1])
                     
def main():
    input = sys.stdin.readline
    startPoint, findPoint = map(int, input().split())
    bfs(startPoint, findPoint)
    
if __name__ == "__main__":
    main()