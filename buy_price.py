a = int(input("price(Baht): "))
b = int(input("discount(%): "))
c = a*b/100
d = a - c
print("discount = %.2f Baht \nprice before discount = %.2f Baht" % (c, d))