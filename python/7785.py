import sys

n = int(sys.stdin.readline())

current_employees = set()

for _ in range(n):
    name, state = sys.stdin.readline().rstrip().split(" ")
    if state == "enter":
        current_employees.add(name)
    elif state == "leave":
        current_employees.discard(name)

for name in sorted(current_employees, reverse=True):
    print(name)