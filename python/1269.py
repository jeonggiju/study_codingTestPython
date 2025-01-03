n , m = map(int,input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

result = len(a.difference(b)) + len(b.difference(a))
print(result)