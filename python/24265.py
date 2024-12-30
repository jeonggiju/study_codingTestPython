'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1 (n-1)
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;

i = 1 j = n-1
i = 2 j = n-2
i = 3 j = n-3
...
i = n-1 j = 1

}
(n-1)(n-2)/2
첫째 줄에 코드1 의 수행 횟수를 출력한다.

둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다.
'''

i = int(input())

n = (i)*(i-1)//2
print(n)
print(2)
