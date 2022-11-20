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
user_choice = int(input("Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS\nyour choice:"))
if user_choice > 2:
    print("Wrong choice!!! \n You lose")
else:
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
    computer_choice = random.randint(0, 2)
    print(f"Computer:{computer_choice}")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)
    if computer_choice == 0 and user_choice == 2:
        print("You lose!!")
    elif computer_choice == 1 and user_choice == 0:
        print("You lose!!")
    elif computer_choice == 2 and user_choice == 1:
        print("You lose!!")
    else:
        print("You Win!!!!!")