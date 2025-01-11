a, b = map(int, input().split())

def gcd(a,b):
    while a != 0:
        나머지 = b % a
        b = a
        a = 나머지
    return b

print(a*b // gcd(a,b))
