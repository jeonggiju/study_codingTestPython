h, m = list(map(int, input().split()))
am = int(input())

m = m + am

h = h + m // 60
m = m % 60

if(h == 24):
    h = 0
if(m == 60):
    m = 0 
    h += 1
print(h , m)