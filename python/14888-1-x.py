import sys

operatorSet = []
visited = [False] * 11
keep = [] 
    
def cal(operandList, operatorList):
    operandIdx = 0
    result = operandList[operandIdx]

    while operandIdx < len(operatorList):
        operandIdx+=1
        operator = operatorList[operandIdx-1]
        if operator == '+':
            result += operandList[operandIdx]
        if operator == '-':
            result -= operandList[operandIdx]
        if operator == '*':
            result *= operandList[operandIdx]
        if operator == '/':
            right = operandList[operandIdx]
            if result < 0:
                result = (-1)*result // right
            else:
                result //= right
    return result

def dfs(num,arr, numOfOperator,idx):
    if idx == numOfOperator :
        # print(arr)
        keep.append(cal(num, arr))
        return
    
    for i in range(numOfOperator):
        if not visited[i]:
            visited[i] = True
            arr[idx] = operatorSet[i] 
            dfs(num, arr, numOfOperator, idx+1)
            visited[i] = False

def main():
    input = sys.stdin.readline
    
    numOfInt = int(input()) # 정수 개수 입력
    num = list(map(int,input().split())) # 정수 입력
    
    # 연산자 입력
    plus, minus, multi, divide = map(int, input().split()) 
    for _ in range(plus):
        operatorSet.append('+')
    for _ in range(minus):
        operatorSet.append('-')
    for _ in range(multi):
        operatorSet.append('*')
    for _ in range(divide):
        operatorSet.append('/')

    arr = [0] * (numOfInt-1) 
    dfs(num,arr, numOfInt-1,0)
    print(max(keep))
    print(min(keep))

if __name__ == "__main__":
    main()