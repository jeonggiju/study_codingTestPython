from collections import deque

def dfs(graphList, visited, startVertex):
    if visited[startVertex] == False:
        print(startVertex + 1, end=" ")
        visited[startVertex] = True
        for i in range(len(graphList)):
            if graphList[startVertex][i] > 0:
                dfs(graphList, visited, i)

def bfs(graphList, startVertex):
    visited = [False for _ in range(len(graphList))]
    queue = deque()
    queue.append(startVertex)
    
    while queue:
        nextIndex = queue.popleft()
        if visited[nextIndex] == False:
            visited[nextIndex] = True
            print(nextIndex + 1, end=" ")
            for i in range(len(graphList)):
                if graphList[nextIndex][i] > 0 and visited[i] == False:
                    queue.append(i)

def main():
    vertex, edge, startVertex = map(int, input().split())
    
    edgeInfo = [list(map(int, input().split())) for _ in range(edge)]
    graphList = [[0] * vertex for _ in range(vertex)]
    
    # 양방향 그래프 구성
    for i in range(len(edgeInfo)):
        graphList[edgeInfo[i][0]-1][edgeInfo[i][1]-1] = 1
        graphList[edgeInfo[i][1]-1][edgeInfo[i][0]-1] = 1

    visited = [False for _ in range(vertex)]

    dfs(graphList, visited, startVertex-1)
    print()
    bfs(graphList, startVertex-1)

if __name__ == "__main__":
    main()
