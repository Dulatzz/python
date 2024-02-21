def areaoftrapezoid(a, b, h):
    return (a+b)*h/2

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print ("Expected Output:", areaoftrapezoid(a, b, h))