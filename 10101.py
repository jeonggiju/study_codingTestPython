x = int(input())
y = int(input())
z = int(input())

if x + y + z != 180:
    print("Error")
    exit(0)


elif x == y == z:
    print("Equilateral")


elif x != y and x!=z and y!=z:
    print("Scalene")
    exit(0)

else:
    print("Isosceles")