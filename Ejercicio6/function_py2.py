def is_leap(year):
    if (year % 4 != 0):
        leap = False
    elif (year % 4 == 0 and (year % 100 == 0 and year % 400 != 0)):
        leap = False
    # Write your logic here
    else:
        leap = True
    return leap

year = int(raw_input())
print (is_leap(year))