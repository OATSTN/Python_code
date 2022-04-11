c = float(input("C = "))
t = input("Temperature unit: ")
if t == "f" or t == "F":
    f = (9/5)*c + 32
    print("F = %.2f" % f)
elif t == "k" or t == "K":
    k = c + 273.15
    print("K = %.2f" % k)
else:
    print("Error")