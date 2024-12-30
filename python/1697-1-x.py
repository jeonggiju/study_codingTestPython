import sys
from collections import deque

def bfs(startPoint, findPoint):
    queue = deque()
    queue.append(startPoint)
    count = 0
    while True:
        current = queue.popleft()
        count+=1
        if current == findPoint:
            break
        queue.append(current*2)
        queue.append(current-1)
        queue.append(current+1)
    checkNum = 0
    weight = -1
    
    while True:
        if count <= checkNum:
            return weight
        weight += 1
        checkNum += 3**weight
        
def main():
    input = sys.stdin.readline
    startPoint, findPoint = map(int, input().split())
    print(bfs(startPoint, findPoint))
    
if __name__ == "__main__":
    main()