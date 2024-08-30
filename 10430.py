# (A+B)%C는 ((A%C) + (B%C))%C
# (A×B)%C는 ((A%C) × (B%C))%C

def sum(a, b):
    return a + b

def mul(a, b):
    return a * b

def mod(a, b):
    return a % b


def main():
    A, B, C = map(int, input().split())
    # (A+B)%C
    print( mod(sum(A,B), C) )
    # ((A%C) + (B%C))%Ca
    print( mod(sum(mod(A,C), mod(B,C)), C) )        
    #  (A×B)%C
    print( mod(mul(A,B), C) )
    # ((A%C) × (B%C))%C
    print( mod(mul(mod(A,C), mod(B,C)), C) )
        
if __name__ == "__main__":
    main()