user = input()
al = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
un = "_"
status = 1
if len(user) >= 4 and len(user) <= 25:
    if user[0].isalpha():
        for i in user:
            if i not in al and i not in num and i not in un:
                status = 0 
        if status == 0:
            print("No")
        else:
            if user.endswith("_"):
                print("No")
            else:
                print("Yes")
    else:
        print("No")
else:
    print("No")