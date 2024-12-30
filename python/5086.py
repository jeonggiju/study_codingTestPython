'''
1. factor: 8 16
2. multiple: 32 % 4 == 0
3. netiher:
'''

nums = []
i = 0

while 1:
    a, b = map(int, input().split())
    if a ==0 and b == 0:
        break
    nums.append([a, b])

for i in range(len(nums)):
    a, b = nums[i][0], nums[i][1],
    if a % b == 0:
        print("multiple")
        continue
    if b % a == 0:
        print("factor")
        continue
    print("neither")
