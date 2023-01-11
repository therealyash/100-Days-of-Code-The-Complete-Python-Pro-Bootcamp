
#Exercise 1 using for loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def go():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for _ in range(6):
    go()
