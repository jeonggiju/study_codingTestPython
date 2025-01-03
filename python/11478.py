str = input()


s = set()
l = len(str)

for i in range(0, l):
    interval = i+1
    for j in range(0,l):
        s.add(str[j:j+interval])

print(len(s))