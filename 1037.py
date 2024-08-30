def main():
    k = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0] * arr[-1])
    
       
if __name__ == "__main__":
    main()