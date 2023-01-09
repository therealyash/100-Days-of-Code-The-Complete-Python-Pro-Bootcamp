'''
Rock Paper Scissor
'''

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
print('Welcome to Rock, Paper & Scissors!')
comp_input = random.randint(0,2)
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_input >= 3 or player_input < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[player_input])
    print(game_images[comp_input])
    if player_input == 0 and comp_input == 2:
        print("You win!")
    elif comp_input == 0 and player_input == 2:
        print("You lose")
    elif comp_input > player_input:
        print("You lose")
    elif player_input > comp_input:
        print("You win!")
    elif comp_input == player_input:
        print("It's a draw")

