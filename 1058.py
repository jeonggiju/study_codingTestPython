def insertArr(arr, item):
    if item not in arr:
        arr.append(item)

def main():
    people= int(input())
    arr = [input() for _ in range(people)]
    
    maxFriend = 0
    for i in range(people):
        checkArr = [False] * people
        
        for j in range(people):
            if i == j: checkArr = [False] * people
        
        for j in range(people):
            if i == j:
                checkArr[j] = True
            
            if(arr[i][j] == 'Y'):
                checkArr[j] = True
                for k in range(people):
                    if(arr[j][k] =='Y'):
                        checkArr[k] = True
        if maxFriend < sum(checkArr):
            maxFriend = sum(checkArr)            
    
    print(maxFriend -1)               
    checkArr[j] = True
            
    if(arr[i][j] == 'Y'):
                checkArr[j] = True
                for k in range(people):
                    if(arr[j][k] =='Y'):
                        checkArr[k] = True
    if maxFriend < sum(checkArr):
            maxFriend = sum(checkArr)            
    
    print(maxFriend -1)                    

if __name__ == "__main__":
    main()