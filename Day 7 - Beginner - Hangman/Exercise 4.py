# Step 4
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6
len_stages = len(stages)

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print('WELCOME TO HANGMAN!')
print(f'Pssst, the solution is {chosen_word}.')

# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
len_chosen_word = len(chosen_word)
display = []
for _ in range(len(chosen_word)):
    display += "_"
print("".join(display))

# guess = input("Guess a letter: ").lower()
#
# for i in range(len_chosen_word):
#     if chosen_word[i] == guess:
#         display[i] = chosen_word[i]
#     else:
#         pass
# print(display)

# TODO-1: - Use a while loop to let the user guess again. The loop
# should only stop once the user has guessed all the letters in the
# chosen_word and 'display' has no more blanks ("_"). Then you can
# tell the user they've won.
print(stages[len_stages-1])
while '_' in display:
    guess = input("Guess a letter: ").lower()
    for i in range(len_chosen_word):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
        else:
            pass
    print("".join(display))

    if guess not in display:
        if len_stages < 1:
            print('Than man is Hanged! Game Over!')
            break
        else:
            len_stages -= 1
            print(stages[len_stages])

else:
    print('You Win! Game Over!')