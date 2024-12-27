'''
높이 V
낮 +A
밤 -B

(A-B)x + A >= V
x >= (V-A)/(A-B)
     A B V
e.g. 2 1 5
'''
import math

A, B, V = map(int, input().split(" "))
x = math.ceil((V-A)/(A-B))

print(x+1)