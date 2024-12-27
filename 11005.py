num, m = map(int, input().split())

# len(list) = 36
list = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

result = ""

while num >= m:
    k = num % m
    result += list[k]
    num = num // m

result += list[num]
print(result[::-1])

# 결과가 뒤집힘