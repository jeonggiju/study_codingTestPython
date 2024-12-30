def ch(n):
    s = 0
    f = len(n)-1
    
    while s < f:
        n[s], n[f] = n[f],n[s]
        s += 1
        f -= 1

    return int(n)
    
s = 'ssaab'
    
print(ch(s))