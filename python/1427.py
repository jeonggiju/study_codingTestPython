import sys


number = int(sys.stdin.readline())

count = [0] * 10

while number != 0:
    count[number % 10] += 1
    number //= 10

for i in range(9, -1, -1):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i ,end="")