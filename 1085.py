'''
1. 한수: (x,y)
2. 좌표: (0,0), (w,h)
'''

x,y,w,h = map(int, input().split(" "))

lst = [x,y, w-x, h-y]
print(min(lst))