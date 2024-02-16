import sys

input = sys.stdin.readline
city = int(input())
graph = [list(map(int, input().split())) for _ in range(city)]
visited = [False] * city
minValue = 10000000

def dfs(startIdx,currentIdx, value, depth):
    global minValue, graph, visited, city
    # 길을 가던 도중 값이 커질 경우 바로 리턴
    if value > minValue:
        return

    # 모든 도시를 한번 씩 방문했고
    if depth == city:
        # 그 와중에 시작점으로 다시 갈 수 있는 경우
        if graph[currentIdx][startIdx]:
            value += graph[currentIdx][startIdx]
            # 값 갱신이 가능하다면 
            if minValue > value:
                minValue = value
        return

    for i in range(city):
        if not visited[i] and graph[currentIdx][i]:
            visited[i] = True
            dfs(startIdx, i, value+graph[currentIdx][i], depth+1)
            visited[i] = False

for i in range(city):
    visited[i] = True
    dfs(i,i,0,1)
    visited[i] = False

print(minValue)