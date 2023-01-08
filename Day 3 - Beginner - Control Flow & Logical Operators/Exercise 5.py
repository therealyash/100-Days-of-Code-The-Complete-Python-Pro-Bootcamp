'''
You are going to write a program that tests the compatibility between two people.
We're going to use the super scientific method recommended by BuzzFeed.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the
word TRUE occurs. Then check for the number of times the letters in the word
LOVE occurs. Then combine these numbers to make a 2 digit number.
'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

def love_calc(name1,name2):

    love_str = (name1 + name2).lower()
    t = love_str.count('t')
    r = love_str.count('r')
    u = love_str.count('u')
    e = love_str.count('e')

    l = love_str.count('l')
    o = love_str.count('o')
    v = love_str.count('v')
    e = love_str.count('e')

    true_score = str(t+r+u+e)
    love_score = str(l+o+v+e)
    love = int(true_score + love_score)

    if love < 10 or love > 90:
        print(f'Your score is {love} & you go together like coke and mentos.')
    elif love > 40 and love < 50:
        print(f'Your score is {love} & you are alright together.')
    else:
        print(f'Your score is {love}.')

love_calc(name1,name2)


