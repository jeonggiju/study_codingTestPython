import sys

input = sys.stdin.readline
n,m = map(int, input().split())
ls = list(map(int, input().split()))
sumTable = [list(map(int, input().split())) for _ in range(m)]

for k in range(m):
    result = sum(ls[sumTable[k][0]-1:sumTable[k][1]])
    print(result)