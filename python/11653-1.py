n = int(input())


prime = [2]


def primeNum(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def addPrime():
    last = prime[-1]

    while True:
        last+=1
        if primeNum(last):
            prime.append(last)
            break


while True:
    if n == 1:
        break;

    if n % 2 == 0:
        print(2)
        n /= 2
        continue

    if n % prime[-1] == 0:
        print(prime[-1])
        n //= prime[-1]
        continue

    addPrime()

