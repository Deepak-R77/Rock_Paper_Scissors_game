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

choices = [rock, paper, scissors]
names = ["rock", "paper", "scissors"]

a = int(input("Choose: 0 for rock, 1 for paper, 2 for scissors → "))

if a > 2:
    print("Invalid number")
else:
    print("You chose:")
    print(choices[a])

    main = random.randint(0, 2)
    print("Computer chose:")
    print(choices[main])

    if a == main:
        print("Draw!")
    elif (a == 0 and main == 2) or (a == 1 and main == 0) or (a == 2 and main == 1):
        print("You win!")
    else:
        print("You lose!")
