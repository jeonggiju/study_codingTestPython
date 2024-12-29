'''
N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 수)
'''

lst = [666]

num = int(input())
i = 1

while True:
    if str(i).find("666") != -1 and lst[-1] < i:
        lst.append(i)

    if len(lst) == num:
        break

    i += 1


print(lst[-1])