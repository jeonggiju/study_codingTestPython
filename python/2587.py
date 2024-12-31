ls = []
for i in range(5):
    ls.append(int(input()))

print(sum(ls)//5)
ls.sort()
print(ls[2])
