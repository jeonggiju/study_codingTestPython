import sys

num = int(sys.stdin.readline())
countLs = [0]*10001

for i in range(num):
    countLs[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if countLs[i] != 0:
        for _ in range(countLs[i]):
            print(i)
