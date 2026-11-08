import random

# ASCII art for the game choices
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

# Store images in a list for easy indexing (0 = Rock, 1 = Paper, 2 = Scissors)
img = [rock, paper, scissors]

# Prompt the user for their choice
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))

# 1. Input Validation: Check for invalid numbers before accessing the list to prevent IndexErrors
if user_input >= 3 or user_input < 0:
    print("You typed an invalid number, you lose!")
else:
    # Display the user's choice
    print("\nYou chose:")
    print(img[user_input])
    
    # Generate and display the computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(img[computer_choice])

    # 2. Game Logic: Determine the winner based on standard Rock-Paper-Scissors rules
    if user_input == computer_choice:
        print("It's a draw!")
    elif user_input == 0 and computer_choice == 2:
        print("You win!")
    elif user_input == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice > user_input:
        print("You lose!")
    elif user_input > computer_choice:
        print("You win!")
