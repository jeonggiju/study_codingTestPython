def change(h, m):
    if(h == 0):
       h = 24
        
    return h*60 + m

def back(m):
    h = (m // 60) % 24
    return [h, m % 60]

h, m = list(map(int, input().split()))
am = int(input())

m = change(h, m+am)

h,m = back(m)

print(h,m)