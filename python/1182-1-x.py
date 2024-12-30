import sys

case = 0 

input = sys.stdin.readline
lenArr, sumOfArr = map(int, input().split())
numOfArr = list(map(int, input().split()))

def dfs(count, result):
    global case
    
    if result == sumOfArr:
        case+=1

    for i in range(count,lenArr):
        result = result + numOfArr[i]
        dfs(i+1, result)
        result = result - numOfArr[i]

dfs(0, 0)
print(case)
