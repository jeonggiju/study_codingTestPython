from collections import deque

n = int(input())
ls = list(map(int, input().split()))
DQ = deque()

for i in range(n):
    DQ.append([i+1, ls[i]])

while DQ:
    value = DQ.popleft()
    print(value[0], end=" ")
    num = value[1]

    if num > 0:
        for i in range(num):
            DQ.append(DQ.popleft())
    else:
        for i in range(-num):
            DQ.appendleft(DQ.pop())
