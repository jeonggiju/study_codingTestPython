import sys

stack = []

def stackPush(x):
    stack.append(x)

input = sys.stdin.readline

num = int(input())

ls = []

for i in range(num):
    ls.append(int(input()))

for i in range(num):
    if ls[i] == 0:
        stack.pop()
    else:
        stack.append(ls[i])

print(sum(stack))