def is_leap(year):
    if year >= 1900 and year <= 10**5:
        if year == 1800 or year == 1900 or year == 2100 or year == 2200 or year == 2300 or year == 2500:
            leap = False
        else:
            if year % 4 == 0:
                leap = True
            elif year % 100 == 0:
                if year % 400 == 0:
                    leap = True
                else:
                    leap = False       
            else:
                leap = False
    return leap

year = int(input())
print(is_leap(year))