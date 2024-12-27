'''
* 쿼터: 0.25
* 다임: 0.10
* 니켈: 0.05
* 페니: 0.01

1.거스름돈은 항상 5달러 이하.
2. 동전의 개수는 최소
e.g. 1.24 => 4쿼더, 2다임, 0니켈, 5페니
'''


num = int(input())
test = []
coin = [25, 10, 5, 1]
for i in range(num):
    test.append(int(input()))

for i in range(len(test)):
    for j in range(0, 4):
        k = test[i] // coin[j]
        test[i] %= coin[j]
        print(k, end=" ")
    print("")

