def is_leap_year(year):
    # Leap year condition:
    # If the year is divisible by 4 and not divisible by 100,
    # or if the year is divisible by 400, it's a leap year.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
