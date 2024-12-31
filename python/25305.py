n,m = map(int, input().split())
ls = list(map(int, input().split()))

ls.sort()
print(ls[n-m])