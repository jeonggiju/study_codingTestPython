import sys

num = int(sys.stdin.readline())
ls = []

for _ in range(51):
    ls.append([])

for i in range(num):
    str = sys.stdin.readline().rstrip('\n')
    if str not in ls[len(str)]:
        ls[len(str)].append(str)

for i in range(len(ls)):
    if len(ls[i]) != 0:
        for j in sorted(ls[i]):
            print(j, end=" ")

