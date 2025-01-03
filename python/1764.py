n ,m = map(int, input().split(" "))

a = set()
b = set()

for i in range(n):
    a.add(input())

for j in range(m):
    b.add(input())

result = a.intersection(b)
print(len(result))

for i in sorted(result):
    print(i)