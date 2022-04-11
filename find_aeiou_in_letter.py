w = input("letter: ")
a = 0
b = 0
c = 0
d = 0
e = 0
for i in w:
    if i in "aA":
        a += 1
    elif i in "eE":
        b += 1
    elif i in "iI":
        c += 1
    elif i in "oO":
        d += 1
    elif i in "uU":
        e += 1
sum = a + b + c + d + e
print("a = %d \ne = %d \ni = %d \no = %d \nu = %d \nTotal = %d" % (a, b, c, d, e, sum))