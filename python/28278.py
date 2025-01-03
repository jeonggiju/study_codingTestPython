import sys
input = sys.stdin.readline

stack = []

def one(x):
    stack.append(x)

def two():
    if len(stack) == 0:
        print(-1)
        return
    val = stack.pop()  # pop() 사용
    print(val)

def three():
    print(len(stack))

def four():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def five():
    if len(stack) == 0:
        print(-1)
        return
    print(stack[-1])

num = int(input())
ls = []

for _ in range(num):
    ls.append(list(map(int, input().split())))

for i in range(num):
    command = ls[i]
    case = command[0]

    if case == 1:
        one(command[1])  # Pass the value directly
    elif case == 2:
        two()
    elif case == 3:
        three()
    elif case == 4:
        four()
    elif case == 5:
        five()
