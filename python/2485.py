n = int(input())

ls = []
for i in range(n):
    ls.append(int(input()))

dif = []
for i in range(n-1):
    dif.append(ls[i+1]-ls[i])

def gcd(a,b):
    # a가 커야함
    if a < b:
        b, a = a, b

    while b != 0:
        a, b = b, a % b
    return a

gcd_v = dif[0]
for i in range(1, len(dif)):
    gcd_v = gcd(gcd_v, dif[i])

print((ls[-1] - ls[0])//gcd_v-(len(ls)-2)-1)

# (ls[-1] - ls[0])//interval-(len(ls)-2)