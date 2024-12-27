'''
1 -> 1 #1 0  ## 1
2-7 -> 2 #6 1 ## 7
8-19 -> 3 #12 2 ## 19
20-37 -> 4 #18 3 ## 37
38-61 -> 5 # 24 4
'''

n = int(input())
num = 1
count = 1

while n > num:
    num += 6*count
    count += 1
print(count)