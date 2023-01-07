# Tip Calculator

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print('Welcome to Tip Calculator!')
bill = float(input('What was the total bill: '))
percent = int(input('What percentage of tip would you like to give 10, 12 or 15: '))
num_ppl = int(input('How many number of people to split the bill: '))
tip = 0
per_person = 0

if percent == 10:
    tip = 0.1 * bill
    per_person = round(tip / num_ppl,2)
    print('Each person should pay:',per_person)
elif percent == 12:
    tip = 0.12 * bill
    per_person = round(tip / num_ppl,2)
    print('Each person should pay:', per_person)
elif percent == 15:
    tip = 0.15 * bill
    per_person = round(tip / num_ppl,2)
    print('Each person should pay:', per_person)
else:
    print('Enter a value between 10,12 & 15!')


