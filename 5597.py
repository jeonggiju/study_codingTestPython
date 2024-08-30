arr = []
범인 = []
for i in range(28):
    arr.append(int(input()))

for i in range(1,31):
    if i not in arr:
        범인.append(i)

for i in range(0,  len(범인)):
    print(범인[i])