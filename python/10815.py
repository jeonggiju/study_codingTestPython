import sys

n = int(sys.stdin.readline().rstrip())
nArr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
m = int(sys.stdin.readline().rstrip())
mArr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

index_nArr = {index: value  for value, index in enumerate(nArr)}

for i in range(len(mArr)):
    try:
         i =  index_nArr[mArr[i]]
         print(1, end=" ")
    except :
        print(0, end=" ")