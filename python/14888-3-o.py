import sys
    
maxValue = -10000000000
minValue = +10000000000
    

def dfs(numOfInt,idx,value,operators, nums):
    global maxValue, minValue
    
    if idx == numOfInt:
        maxValue = max(maxValue, value)
        minValue = min(minValue, value)
    else:
        #덧셈
        if operators[0] > 0:
            operators[0] -= 1
            dfs(numOfInt, idx+1, value+nums[idx], operators, nums)
            operators[0] += 1
        #뺼셈
        if operators[1] > 0:
            operators[1] -= 1
            dfs(numOfInt, idx+1, value-nums[idx], operators, nums)
            operators[1] += 1
        #곱셈
        if operators[2] > 0:
            operators[2] -= 1
            dfs(numOfInt, idx+1, value*nums[idx], operators, nums)
            operators[2] += 1
        #나눗셈
        if operators[3] > 0:
            operators[3] -= 1
            dfs(numOfInt, idx+1, int(value/nums[idx]), operators, nums)
            operators[3] += 1
            
        
    
def main():
    input = sys.stdin.readline
    
    numOfInt = int(input()) # 정수 개수 입력
    nums = list(map(int,input().split())) # 정수 입력
    #add, sub, mul, div
    operators = list(map(int, input().split())) # 연산자 개수 입력
    dfs(numOfInt, 1, nums[0],operators,nums)
    print(maxValue)
    print(minValue)

if __name__ == "__main__":
    main()