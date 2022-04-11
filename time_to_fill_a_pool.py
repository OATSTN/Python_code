w = float(input("Enter width: "))
l = float(input("Enter length: "))
d = float(input("Enter depth: "))
v = w*l*d
t = v*(15/60) #fix flow rate
print("Time to fill a pool is %.2f minutes." % t)