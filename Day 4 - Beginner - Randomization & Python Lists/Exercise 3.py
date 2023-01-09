'''
You are going to write a program which will mark a spot with an X.
The map is made of 3 rows of blank squares.
  1      2      3
Your program should allow you to enter the position of the treasure using a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number.
'''

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#😎💎

# Write your code below this row 👇
row = int(position[0])
col = int(position[1])

# select = map[col - 1]
# select[row - 1] = '💎'
map[col - 1][row - 1] = '💎'
print(f"{row1}\n{row2}\n{row3}")
