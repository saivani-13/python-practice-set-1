l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

if l > 0 and b > 0:
    print("Area:", l * b)
    print("Perimeter:", 2 * (l + b))
else:
    print("Invalid input")