import sys

visited = [False] * 10
arr = [0] * 10

def recur(num, size, idx):
    if idx == size:
        for i  in range(size):
            print(arr[i], end=" ")
        print()
        return

    for i in range(1, num+1):
        if not visited[i] and i > arr[idx-1]:  
                visited[i] = True 
                arr[idx] = i
                recur(num, size, idx+1)
                visited[i] = False

def main():
    input = sys.stdin.readline
    
    num, size = map(int, input().split())
    recur(num, size, 0)
    
    
if __name__ == "__main__":
    main()