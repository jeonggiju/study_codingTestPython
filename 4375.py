
# 2와 5로 나누어 떨어지지 않는 n(1 < n < 10000)
# 자릿수를 출력해야한다.
# 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾아야함.
# 이 때 n의 배수는 가장 작아야함.
def main():
    while True:
        
        try:
            n = int(input())
        except:
            break
        
        digits = 1
        one = 1
        
        while True:
            if(one % n == 0):
                print(digits)
                break
            else:
                digits += 1
                one = one*10 + 1
    
if __name__ == "__main__":
    main()