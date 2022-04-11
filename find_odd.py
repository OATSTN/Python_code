n = int(input("n: "))
if n > 0:
    while n > 0:
        a = n % 10
        print(a)
        n //= 10
else:
    print("ERROR")
x = 0
while True:
    n = int(input("n: "))
    if n < 0:
        break
    else:
        if n % 2 != 0:
            x += 1
print("Received %d odd numbers" % x)