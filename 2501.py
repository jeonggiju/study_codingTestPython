n, k = map(int, input().split())

list=[]

for i in range(1,n+1):
    if n % i == 0:
        list.append(i)
try:
    print(list[k-1])
except IndexError as e:
    print(0)