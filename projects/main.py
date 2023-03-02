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

#Write your code below this line 👇

game_image = [rock, paper, scissors]

players_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
players_choice = int(players_choice)

if players_choice >= 3 or players_choice < 0:
  print("Invalid entry, you lose!")
else:
  print(game_image[players_choice])

  cpu_choice = random.randint(0, 2)
  print("Computer chose:")
  print(game_image[cpu_choice])
  
  
  if players_choice == 0 and cpu_choice == 2:
    print("You win!!!")
  elif cpu_choice == 0 and players_choice == 2:
    print("You lose!")
  elif cpu_choice > players_choice:
    print("You lose!")
  elif players_choice > cpu_choice:
    print("You win!")
  elif players_choice == cpu_choice:
    print("It's a draw!")
  else:
    print("Invalid entry, you lose!")