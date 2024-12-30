import sys

case = 0 

input = sys.stdin.readline
lenArr, sumOfArr = map(int, input().split())
numOfArr = list(map(int, input().split()))
arr = []

def dfs(count):
    global case
    
    if len(arr) > 0 and sum(arr) == sumOfArr:
        case+=1

    for i in range(count,lenArr):
        arr.append(numOfArr[i])
        dfs(i+1)
        arr.pop()

dfs(0)
print(case)
