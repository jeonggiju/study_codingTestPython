nums = []

while 1:
    n= int(input())
    if n ==-1 :
        break
    nums.append(n)


for i in range(len(nums)):
    y = []
    for j in range(1,nums[i]):
        if nums[i] % j == 0:
            y.append(j)

    if sum(y) == nums[i]:
        print(nums[i],"= ",end="")
        for j in range(len(y)-1):
            print(y[j] ,"+ ", end="")
        print(y[-1])

    else:
        print(nums[i],"is NOT perfect.")