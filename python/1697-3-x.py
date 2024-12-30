import sys
from collections import deque

def bfs(startPoint, findPoint):
    queue = deque()
    queue.append([startPoint, 0])
    visited = set()

    while True:
        current = queue.popleft()
        visited.add(current[0])
        print(current)

        if current[0] == findPoint:
            print(current[1])
            return
        
        if current[0]*2 not in visited and current[0]*2 not in queue:
            queue.append([current[0]*2, current[1]+1])
        if current[0]-1 not in visited and current[0]-1 not in queue:
            queue.append([current[0]-1, current[1]+1])
        if current[0]+1 not in visited and current[0]+2 not in visited:
            queue.append([current[0]+1,current[1]+1])
        
def main():
    input = sys.stdin.readline
    startPoint, findPoint = map(int, input().split())
    bfs(startPoint, findPoint)
    
if __name__ == "__main__":
    main()