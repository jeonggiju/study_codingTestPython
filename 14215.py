'''
* 삼각형의 조건 제일 긴 변의 길이가 나머지 두 변의 길이의 합보다 작아야한다. 같으면 안됨
'''

lst = list(map(int, input().split(" ")))

lst.sort()


while lst[2] >= lst[0]+lst[1]:
    lst[2] -= 1

print(sum(lst))