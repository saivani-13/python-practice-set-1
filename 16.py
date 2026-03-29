a = float(input())
b = float(input())
c = float(input())

d = b*b - 4*a*c

if d > 0:
    print("Real and distinct")
elif d == 0:
    print("Real and equal")
else:
    print("Complex")