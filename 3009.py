x_lst = []
y_lst = []


def getRest(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) == 1:
            return lst[i]

for i in range(3):
    x, y = map(int, input().split(" "))
    x_lst.append(x)
    y_lst.append(y)

print(getRest(x_lst), getRest(y_lst))