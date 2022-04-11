t = input("Enter your buffet choice: ")
if t == "Japanese":
    d = input("Is today Wednesday (yes/no): ")
    if d == "yes":
        p = 1000 - 1000*0.15
        print("Your payment is %.2f bath" % p)
    else:
        p = 1000
        print("Your payment is %.2f bath" % p)
elif t == "Korean":
    d = input("Is today Wednesday (yes/no): ")
    if d == "yes":
        p = 1500 - 1500*0.15
        print("Your payment is %.2f bath" % p)
    else:
        p = 1500
        print("Your payment is %.2f bath" % p)
else:
    print("Sorry, there is no Thai buffet.")