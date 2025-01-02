n = int(input())

myCard = {}

ls = list(map(int, input().split(" ")))

for i in range(n):
    number = ls[i]
    if number in myCard:
        myCard[number] += 1
    else:
        myCard[number] = 1

m = int(input())

arr = list(map(int, input().split(" ")))

for i in range(m):
    try:
        print(myCard[arr[i]], end=" ")
    except:
        print(0, end=" ")
