import sys

# 45
checkSet = [1,2,3,4,5,6,7,8,9]
input = sys.stdin.readline
# graph = [list(map(int, input().split())) for _ in range(9)]
# print(graph)


if sorted([2,3,4,5,6,7,8,9,1]) == checkSet:
    print("ok")
else:
    print("no")
