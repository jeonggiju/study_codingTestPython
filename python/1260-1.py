import sys

def dfs(edgeInfo, visited, startIdx):
    visited[startIdx] = True
    print(startIdx, end=" ")
    
    for i in edgeInfo[startIdx]:
        if not visited[i]:
            dfs(edgeInfo, visited, i)

def bfs(edgeInfo, visited, startIdx):
    queue = [startIdx]
    
    while queue:
        nextIdx = queue.pop(0)
        if not visited[nextIdx]:
            print(nextIdx, end=" ")
            visited[nextIdx] = True
            for i in edgeInfo[nextIdx]:
                queue.append(i)

def main():
    input = sys.stdin.readline
    
    vertex, edge, startIdx = map(int,input().split())
    
    edgeInfo = [[] for _ in range(vertex+1)]
    
    for _ in range(edge):
        n, v = map(int, input().split())
        edgeInfo[n].append(v)
        edgeInfo[v].append(n)
        
    for lst in range(len(edgeInfo)):
        edgeInfo[lst].sort()

    visited = [False] * (vertex+1)
    dfs(edgeInfo, visited, startIdx)
    print()
    visited = [False] * (vertex+1)
    bfs(edgeInfo, visited, startIdx)
        
    
if __name__ == "__main__":
    main()