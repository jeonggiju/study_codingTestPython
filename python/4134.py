num = int(input())

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime(n):

    while not is_prime(n):
        n += 1

    return n


ls = []
for i in range(num):
    ls.append(int(input()))

for i in range(num):
    print(get_prime(ls[i]))