from collections import deque

dq = deque()

def discard():
    if len(dq) != 1:
        dq.popleft()
        return 0
    else:
        return -1

def change():
    dq.append(dq.popleft())

n = int(input())

for i in range(1,n+1):
    dq.append(i)

while True:
    if discard() == -1:
        break
    change()

print(dq[0])
