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

# choices = [rock, paper, scissors]

# user_choice = input("What do you choose? Type 0 for Rock, 1 for paper, or 2 for Scissors. ")
# if user_choice == "0":
#   print(rock)
# elif user_choice == "1":
#   print(paper)
# else:
#   print(scissors)

# print("Computer chose:")
# computer_choice = random.randrange(len(choices))
# if computer_choice == "0":
#    print(rock)
# elif computer_choice == "1":
#   print(paper)
# else:
#   print(scissors)



# if user_choice == 1 and computer_choice == 0:
#    print("You win!")
# elif user_choice == 0 and computer_choice == 1:
#   print("You lose.")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif user_choice == 1 and computer_choice == 0:
#   print("You win!")
# elif user_choice == 0 and computer_choice == 2:
#   print("You lose.")
# else:
#  print("It's a draw.")


#Above was my attempt at solving this scenario
#Below will be the solution following the instructor

choices = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper, or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose.")
else:
  print(choices[user_choice])

  computer_choice = random.randint(0, 2)
  print("Computer chose:")
  print(choices[computer_choice])
  if user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose.")
  elif computer_choice > user_choice:
    print("You lose.")
  elif user_choice > computer_choice:
    print("You win!")
  elif computer_choice == user_choice:
    print("Its a draw!")

#I got pretty close in my attempted solution-- I had all the right ideas
#I struggled with cleaning up the logic, a big part of which is that
#though I tried multiple times to avoid an else statement, and only use
#elif to define the conditions, I didn't realize that placing that line at the
#end of the block was preventing it from ever being checked
#I also complicated the random generation for the computer choice; though
#what I attempted works, it is more applicable to a large set of data
