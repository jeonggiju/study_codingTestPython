
def main():
    # 자연수 n은 생성자 
    n = int(input())
    countNum = n
    count = 0 # 자리수

    while countNum!=0:
        countNum //=10
        count+= 1
# abc + a+ b+ c = x
    result = []
    digit = []
    a = 1
    while(a < n):
        # 배열 0으로 초기화
        digit = [0 for i in range(count)]
        
        # 나눌 숫자 100에서 시작
        divide = 10
        
        forA = a
        for i in range(0, count):
            num =  forA % divide
            digit[i] = num
            forA //= 10
            
        sum = a
        
        for i in range(0, count):
            sum += digit[i]
        
        if sum==n:
            print(a)
            return
        a += 1
    print(0)


if __name__ == "__main__":
    main()