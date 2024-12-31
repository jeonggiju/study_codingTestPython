import sys

num=int(input())
numbers=[]
for i in range(num):
    numbers.append(int(sys.stdin.readline()))
for i in sorted(numbers):
    print(i)
