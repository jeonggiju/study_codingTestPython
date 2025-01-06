import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
DQ = deque()
for _ in range(N):
    S = sys.stdin.readline().split()

    if S[0] == '1':
        DQ.appendleft(int(S[1]))

    if S[0] == '2':
        DQ.append(int(S[1]))
    if S[0] == '3':
        if not DQ:
            print("-1")
        else:
            print(DQ.popleft())
    if S[0] == '4':
        if not DQ:
            print("-1")
        else:
            print(DQ.pop())
    if S[0] == '5':
        print(len(DQ))
    if S[0] == '6':
        if DQ:
            print("0")
        else:
            print("1")
    if S[0] == '7':
        if DQ:
            print(DQ[0])
        else:
            print(-1)
    if S[0] == '8':
        if DQ:
            print(DQ[-1])
        else:
            print(-1)