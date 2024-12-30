import sys

n = int(input())
nums = list(map(int, input().split()))
opchck = list(map(int, input().split()))
mx = None
mn = None

ops = []

def dfs():
    global mx, mn
    
    if len(ops) == n-1:
        opcnt = [0, 0, 0, 0]

        for op in ops:
            opcnt[op] += 1
            
        for op in range(4):
            if opcnt[op] != opchck[op]:
                return

        val = calc()

        if mx is None:
            mx = val
        else:
            mx = max(mx, val)
            
        if mn is None:
            mn = val
        else:
            mn = min(mn, val)

    else:
        for op in range(4):
            ops.append(op)
            dfs()
            ops.pop()

def calc():
    out = nums[0]
    
    for i in range(n-1):
        if ops[i] == 0:
            out += nums[i+1]
        elif ops[i] == 1:
            out -= nums[i+1]
        elif ops[i] == 2:
            out *= nums[i+1]
        else:
            if out < 0:
                out = -(-out//nums[i+1])
            else:
                out = out//nums[i+1]

    return out

dfs()

print(mx)
print(mn)
