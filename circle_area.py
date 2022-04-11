import math
r = int(input("Enter a radius: "))
a = math.pi*r**2
l = 2*math.pi*r
print("Area of a circle with radius %d is %.2f \nCircumference of a circle with radius %d is %.2f" % (r, a, r, l))