import math

def areaofregularpolygon(n, l):
    if n == 4:
        return l*l
    r = math.sqrt(l*l/(2-2*math.cos(360/n)))
    return (n/2)*l*r

n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

print("The area of the polygon is:", areaofregularpolygon(n, l))