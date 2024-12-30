import sys

input = sys.stdin.readline
lenArr,target = map(int, input().split())
numOfArr = list(map(int, input().split()))
cnt = 0
arr = []


def recur(startIdx):
    global cnt
    if sum(arr) == target and len(arr) >0:
        cnt += 1
        
    for i in range(startIdx, lenArr):
        arr.append(numOfArr[i])
        recur(i+1)
        arr.pop()

recur(0)
print(cnt)