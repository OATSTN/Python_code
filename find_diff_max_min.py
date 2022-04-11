min = 1000
max = 0
while True:
    n = float(input("n: "))
    if n >= 0:
        if n < min:
            min = n
        elif n > max:
            max = n 
    else:
        break
diff = max - min
print(diff)