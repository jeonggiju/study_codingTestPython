import sys
from collections import deque

def bfs(startPoint, findPoint):
    queue = deque()
    queue.append(startPoint)
    maxNum = 100000 
    visited = [0] * (maxNum+1)

    while queue:
        current = queue.popleft()

        if current == findPoint:
            print(visited[current])
            break
        
        if current > 0 and not visited[current-1]:
            visited[current-1] = visited[current]+1
            queue.append(current-1)
            
        if current < findPoint:
            if not visited[current+1]:
                visited[current+1] = visited[current] + 1
                queue.append(current+1)
            if not visited[current*2]:
                visited[current*2] = visited[current] + 1
                queue.append(current*2)
        
        # 이거 순서 다르면 틀림...ㅠㅠㅠ 왜??? 씨ㅡ발 왜죠?
        # # for j in  (current*2,current-1, current+1):
        # for j in  (current-1, current+1,current*2):
        #     if 0<= j <= maxNum and not visited[j]:
        #         visited[j] = visited[current]+1
        #         queue.append(j)
def main():
    input = sys.stdin.readline
    startPoint, findPoint = map(int, input().split())
    bfs(startPoint, findPoint)
    
if __name__ == "__main__":
    main()