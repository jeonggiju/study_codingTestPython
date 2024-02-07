def main():
    s1, s2, s3 = map(int, input().split())

    value = [0] * (s1 + s2 + s3 + 1)

    for i in range(1, s1+1):
        for j in range(1, s2+1):
            for k in range(1, s3+1):
                value[i + j + k] += 1    
                
    max = 2
    for i in range(3, len(value) + 1):
        if value[i] > value[max]:
            max = i
        else:
            break
    print(max)

if __name__ == "__main__":
    main()