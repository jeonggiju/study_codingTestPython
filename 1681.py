def digitCheck(checkNum, L):
    while checkNum > 0:
        if checkNum % 10 == L:
            return False
        checkNum /= 10
    return True

    # 자리수 구하기
    count = 0
    number = checkNum
    while number > 0:
        number //= 10
        count += 1
    
    # 각 자리 검사(있으면 1, 없으면 0)
    a = 10 ** (count)
    while count  != 0:
        digit = (checkNum % a) // (a // 10)
        if(digit == L):
            return True
        else:
            a //= 10
            count -= 1
    
        
    return False

def main():
# 10 1 
# 1 2 3 4 5 6 7 8 9 10 -> 8번
# 11 12 13 14 15 16 17 18 19 20 -> 1번 
# 21 22 23 24 25 26 27 28 29 30 -> 

    N, L = map(int, input().split())
    count = 0
    value = 1
    while True:
        # 올라가는 숫ㅈ
        digitBoolean = digitCheck(value,L)
        # 없을 경우
        if(digitBoolean != 1):
            count+=1
            
        if(count == N):
            break
        else:
            value += 1

    print(value)

if __name__ == "__main__":
    main()