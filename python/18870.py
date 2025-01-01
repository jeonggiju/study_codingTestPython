import sys

num = int(sys.stdin.readline())
ls = list(map(int, (sys.stdin.readline().rstrip().split(" "))))
uni_ls = sorted(set(ls))

index_dic = {index: value  for value, index in enumerate(uni_ls)}

for i in ls:
    print(index_dic[i], end=" ")
