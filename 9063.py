x_lst = []
y_lst = []

n = int(input())

for i in range(n):
    x,y  = map(int, input().split(" "))
    x_lst.append(x)
    y_lst.append(y)

x_max = max(x_lst)
x_min = min(x_lst)
y_max = max(y_lst)
y_min = min(y_lst)

print((x_max-x_min) * (y_max-y_min))