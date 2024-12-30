'''
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2
        for j <- i + 1 to n - 1
            for k <- j + 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

1. n - 2 -1 + 1 = n-2 <- i
2. n - 1 - i - 1 + 1 = n-i-1 <- j
3. n - j - 1 + 1 = n-j <- k



'''


n = int(input())
print(n*(n-1)*(n-2)//6)
print(3)