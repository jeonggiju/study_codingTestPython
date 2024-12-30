# row 11, col 10, sizeSize 2
def findSquare(arr, row, col,sideSize):
    for i in range(0, row-sideSize+1):
        for j in range(0, col-sideSize+1):
            if arr[i][j] == arr[i+sideSize-1][j+sideSize-1]:
                if arr[i][j] == arr[i+sideSize-1][j] and arr[i][j] == arr[i][j+sideSize-1]:
                    return 1
    return 0

def main():
    row, col = map(int, input().split())
    arr = [input() for _ in range(row)]
    maxSize = 1
    
    if row > col:
        min = col
    else:
        min = row
    
    for i in range(2, min+1):
        if findSquare(arr, row, col, i) == 1:
            maxSize = i
    
    print(maxSize* maxSize)            
    
if __name__ == "__main__":
    main()