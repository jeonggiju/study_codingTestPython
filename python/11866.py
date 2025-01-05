n, k = map(int,input().split() )

qu = [i+1 for i in range(n)]

res = []
while len(qu):
    for _ in range(k-1):
        qu.append(qu.pop(0))
    res.append(qu.pop(0))

print("<", end='')
print(', '.join(map(str,res)), end='')
print(">")