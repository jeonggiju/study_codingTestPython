r = int(input())
c = int(input())
s = 0
for _ in range(c):
    p, n = list(map(int, input().split()))
    s += p * n
    
if(s != r):
    print('No')
else:
    print("Yes")