'''
Write a program that works out whether if a given year is a leap year. A normal
year has 365 days, leap years have 366, with an extra day in February.
This is how you work out whether if a particular year is a leap year.
On every year that is evenly divisible by 4 **except** every year that is evenly
divisible by 100 **unless** the year is also evenly divisible by 400
'''

year = int(input('Enter an year to check if it is a leap year: '))
year_status = ''
def display(a):
    print('The year is',a)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            year_status = 'Leap Year'
            display(year_status)
        else:
            year_status = 'Not Leap Year'
            display(year_status)
    else:
        year_status = 'Leap Year'
        display(year_status)

else:
    year_status = 'Not Leap year'
    display(year_status)