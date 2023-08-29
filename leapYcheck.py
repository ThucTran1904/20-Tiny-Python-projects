def leap_year_check(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('This is a leap year')
            else:
                print('This is not a leap year')
        else:
            print('This a extremely a leap year')
    else:
        print('This is not a leap year')

input_year = int(input('Input the year that u want to check: '))
leap_year_check(input_year)