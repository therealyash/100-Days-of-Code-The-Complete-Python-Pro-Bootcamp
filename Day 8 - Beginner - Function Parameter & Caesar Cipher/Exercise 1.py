'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
number of cans = (wall height ✖️ wall width) ÷ coverage per can.
e.g. Height = 2, Width = 4, Coverage = 5
number of cans = (2 ✖️ 4) ÷ 5
                     = 1.6
                     = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
'''

# Write your code below this line 👇
import math
def paint_area(h,w,cover):
    num_cans = math.ceil((h*w)/cover)
    return print('No. of cans required:',num_cans)

h = int(input('Enter the height: '))
w = int(input('Enter the weight: '))
paint_area(h,w,cover = 5)
