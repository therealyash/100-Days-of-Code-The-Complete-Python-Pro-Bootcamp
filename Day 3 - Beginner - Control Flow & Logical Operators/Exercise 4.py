'''
Congratulations, you've got a job at Python Pizza.
Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''
print('Welcome to Python Pizza!')
print('Please select the type of Pizza below!')
size = input("Which size of pizza ? S, M or L : ")
pepperoni = input("Do you want pepperoni? Y or N : ")
cheese = input("Do you want extra cheese ? Y or N : ")

bill = 0

def display(a):
    print(f'Your bill value is ${a}.')

if size == 'S':
    bill = 15
    if pepperoni == 'Y':
        bill = bill + 2
        if cheese == 'Y':
            bill = bill + 1
            display(bill)
        elif cheese == 'N':
            display(bill)
    elif pepperoni == 'N':
        if cheese == 'Y':
            bill = bill + 1
            display(bill)
        elif cheese == 'N':
            display(bill)

if size == 'M':
    bill = 20
    if pepperoni == 'Y':
        bill = bill + 3
        if cheese == 'Y':
            bill = bill + 1
            display(bill)
        elif cheese == 'N':
            display(bill)
    elif pepperoni == 'N':
        if cheese == 'Y':
            bill = bill + 1
            display(bill)
        elif cheese == 'N':
            display(bill)

if size == 'L':
    bill = 25
    if pepperoni == 'Y':
        bill = bill + 3
        if cheese == 'Y':
            bill = bill + 1
            display(bill)
        elif cheese == 'N':
            display(bill)
    elif pepperoni == 'N':
        if cheese == 'Y':
            bill = bill + 1
            display(bill)
        elif cheese == 'N':
            display(bill)



