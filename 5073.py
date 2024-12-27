def check(x,y,z):
    lst = [x,y,z]
    if  max(lst) >= sum(lst)-max(lst):
        print("Invalid")
    elif x == y == z:
        print("Equilateral")
    elif x != y and x!=z and y!=z:
        print("Scalene")
    else:
        print("Isosceles")


lst = []
while True:
    x,y,z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    lst.append([x,y,z])


for i in range(len(lst)):
    check(lst[i][0],lst[i][1],lst[i][2])