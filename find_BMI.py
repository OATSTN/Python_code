w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
BMI = w/h**2
if BMI < 18.5:
    print("BMI is %.1f \nUnderweight" % BMI)
elif BMI >= 18.5 and BMI < 25:
    print("BMI is %.1f \nNormal weight" % BMI)
elif BMI >= 25 and BMI < 30:
    print("BMI is %.1f \nOverweight" % BMI)
else:
    print("BMI is %.1f \nObesity" % BMI)