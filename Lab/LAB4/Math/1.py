import math

def degreetoradian(n):
    return n*math.pi/180

n = int(input("Input degree: "))

print("Output radian:", degreetoradian(n))