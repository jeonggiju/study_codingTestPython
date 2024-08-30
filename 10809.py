s = str(input())
arr = [-1] * 26

for i in range(len(s)):
    if(arr[ord(s[i])-97]==-1):
            arr[ord(s[i])-97] = i
    

for i in range(26):
    print(arr[i], end=" ")
