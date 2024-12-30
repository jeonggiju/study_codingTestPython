'''
- ax + by = c
    - y = (c-ax)//b
- dx + ey = f
    - y = (f-dx)//e

- b(f-dx) = e(c-ax)

'''


a,b,c,d,e,f = map(int,input().split())


x= None
y= None
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i + b*j == c )  and  (d*i + e*j == f):
            x = i
            y = j
            break
    if x is not None and y is not None:
        break


print(x, y)

