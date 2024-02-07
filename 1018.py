def startBlackChess(inputChess, n, m):
    count = 0
    color = 'B'
    for i in range(n,n+8):
        for j in range(m,m+8):
            if color != inputChess[i][j]:
                count += 1
            
            if color == 'B':
                color = 'W'
            else:
                color  = 'B'
        if color == 'B':
            color = 'W'
        else:
            color  = 'B'        
    
    return count
            
            
def startWhiteChess(inputChess, n, m):
    count = 0
    color = 'W'
    for i in range(n,n+8):
        for j in range(m,m+8):
            if color != inputChess[i][j]:
                count += 1
            
            if color == 'B':
                color = 'W'
            else:
                color  = 'B'
        if color == 'B':
            color = 'W'
        else:
            color  = 'B'        
    
    return count
                        

def main():
    N, M = map(int, input().split())
    
    inputChess = [input() for _ in range(N)]
    countN = N - 7
    countM = M - 7
    
    result = [63, 63]
    minResult = 63
    for i in range(countN):
        for j in range(countM):
            result[0] = startBlackChess(inputChess, i, j)
            result[1] = startWhiteChess(inputChess, i, j)
            if minResult > min(result[0],result[1]):
                minResult = min(result[0],result[1])
            

    print(minResult)
if __name__ == "__main__":
    main()