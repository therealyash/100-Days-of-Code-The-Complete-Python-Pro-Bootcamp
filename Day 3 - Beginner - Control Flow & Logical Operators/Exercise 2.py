'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.
'''

height = float(input("Enter height in metres : "))
weight = float(input("Enter weight in kgs : "))

bmi = round(weight/height**2,1)
bmi_status = ''

def display(a, b):
    print('Your BMI is {a}, you are {b}.'.format(a = a,b = b))

if bmi <= 18.5:
    bmi_status = 'Underweight'
    display(bmi,bmi_status)
elif bmi > 18.5 and bmi < 25:
    bmi_status = 'Normal Weight'
    display(bmi, bmi_status)
elif bmi > 25 and bmi < 30:
    bmi_status = 'Slightly Overweight'
    display(bmi, bmi_status)
elif bmi > 30 and bmi < 35:
    bmi_status = 'Obese'
    display(bmi, bmi_status)
elif bmi > 35:
    bmi_status = 'Clinically Obese'
    display(bmi, bmi_status)


    






