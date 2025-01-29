a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

a = a1 * b2 + b1 * a2
b = a2 * b2

def gcd(a,b): # b > a
    if b < a:
        a, b = b, a

    while a != 0:
        나머지 = b % a
        b = a
        a = 나머지
    return b

gcdRe = gcd(a,b)

print(a//gcdRe, b//gcdRe)