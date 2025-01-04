n = int(input())

qu = list(map(int, input().split()))
st = []
i = 1

for i in qu:
    st.append(i)

    while st and st[-1] == i:
        st.pop()
        i+=1

if st:
    print("Sad")
else:
    print("Nice")


