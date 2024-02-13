import sys

arr = [0]* 10

def recur(n,m,idx):
    if idx == m:
        for i in range(idx):
            print(arr[i], end=" ")
        print()
        return    

    for i in range(1, n+1):
        if arr[idx-1] <= i:
            arr[idx] = i
            recur(n,m, idx+1)

def main():
    input = sys.stdin.readline
    
    n,m = map(int, input().split())
    recur(n,m,0)
    

if __name__ == "__main__":
    main()