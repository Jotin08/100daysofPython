print('''
           (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""`

''')
print("Welcome to Jotin's Coffee Shop.")
print("We only serve coffee one way. Order anything elae and you're out of here. This ain't Starbucks!") 

choice1 = input("What would you like to have?\n'Caf' or 'Decaf'?\n").lower()
if choice1 == "caf":
  choice2 = input("I like you style. Would you like cream with that? 'Yes' or 'No'?\n").lower()
  if choice2 == "no":
    choice3 = input("Great! Final question...'drip', 'pour-over', or 'cold brew'?\n").lower()
    if choice3 == "drip":
      print("No drip here!\nGame Over!")
    elif choice3 == "pour-over":        
      print("Pour-over? Wrong answer!\n")
    elif choice3 == "cold brew":
      print("Quick to drink, refreshing, and more caffeine to take on anything. Cold brew coming right up?\nYou win!!!")
    else:
      print("It's cold brew or nothing!!!")
  else:
      print("No cream!!!\nGame Over")
else:
        print('Decaf? Would you like some orange-free orange juice with that?!\nGame over!')
#need to refine this later to add some random string logic

