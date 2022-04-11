s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))
s3 = s1 + s2
a = s3 // 3600
b = (s3 % 3600) // 60
c = s3 % 60
print("It is %d hours %d minutes and %d second" % (a, b, c))