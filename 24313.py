'''
O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
f(n) = a1*n + a0
a1 a0
c
n0

7 7
8
1

f(n) = 7n + 7
g(n) = n
c * g(n) = 8 * n
c = 8
n0 = 1
'''

aOne, aZero = map(int, input().split())
c = int(input())
nZero = int(input())

if (aOne * nZero + aZero) <= c * nZero and aOne <= c:
    print(1)
else:
    print(0)

