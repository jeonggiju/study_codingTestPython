n, m = map(int, input().split())

nLs = [input() for _ in range(n)]
mLs = [input() for _ in range(m)]

indexLs = {value: index for index, value in enumerate(nLs)}

s = 0

for i in mLs:
    if i in indexLs:
        s += 1

print(s)
