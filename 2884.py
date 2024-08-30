def change(h, m):
    if(h == 0 and m < 45):
       h = 24
        
    return h*60 + m

def back(m):
    return [m // 60, m % 60]

h, m = list(map(int, input().split()))


hh,mm = back(change(h,m) - 45)
print(hh, mm)