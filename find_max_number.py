a = int(input("n1: "))
b = int(input("n2: "))
c = int(input("n3: "))
if a == b and b == c:
    print("%d = %d = %d" % (a, b, c))
else:
    if a > b and a > c or b == c :
        if b < c:
            print("%d > %d: %d" % (a, b, a - b))
        elif c < b:
            print("%d > %d: %d" % (a, c, a - c))
        else:
            print("%d > %d and %d: %d" % (a, b, c, a - b))
    elif b > a and b > c or a == c:
        if a < c:
            print("%d > %d: %d" % (b, a, b - a))
        elif c < a:
            print("%d > %d: %d" % (b, c, b - c))
        else:
            print("%d > %d and %d: %d" % (b, a, c, b - a))
    else:
        if a < b:
            print("%d > %d: %d" % (c, a, c - a))
        elif b < a:
            print("%d > %d: %d" % (c, b, c - b))
        else:
            print("%d > %d and %d: %d" % (c, a, b, c - a))