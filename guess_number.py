target = 72
x = 0
while True:
    n = int(input("Enter your guess: "))
    x += 1
    if n == target:
        break
    elif n > target and n <= 100:
        print("Sorry, your guess is too high")
    elif n < target and n >= 0:
        print("Sorry, your guess is too low")
    else:
        print("Sorry, your guess is out of range")
print("Congratulations, your is guess correct. Total number of guesses is %d" % x)