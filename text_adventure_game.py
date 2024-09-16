print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

choice1 = input('There are two paths ahead of you.\nThe left path looks worn out, as if there is a lot of foot traffic passing through.\nThe right path looks overgrown, with tall grass and shubbery littered along the path.\nType "left" to go down what looks like the more used path, or "right" to force your way through the forest.\n').lower()

if choice1 == "left":
  choice2 = input('You come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input('You wait 20 minutes, and eventually a boat comes to shore. \nYou are ferried to the island, where you are left alone.\nYou spot a campfire in the distance, but you also see what looks like a cave.\nType "campsite" to go search for people, or "cave" to explore the cave\n').lower()
    if choice3 == "cave":
      choice4 = input('You walk into the cave, and flick on your flashlight.\nYou walk a couple hundred feet in to the narrowing cave.\nRight when you think that this is pointless, you find box on the ground.\nYou pick the box up and inspect it. Is this the treasure you heard about?\nHowever, something feels off about this situation. \nPlus, you agreed to unbox the treasure with your friends, if you found it.\nDo you still want to open it? Type "open" to open the box, or "wait" to wait until later\n').lower()
      if choice4 == "wait":
        print('Trusting your instict, you exit the cave bringing the box with you. \nOnce you are in the sunlight again, you wait patiently for the boat to come back around.\nYou head back to the village, and in the company of your friends, open the box. \nAs you do, an ominous spirit appears, but disappears after saying only a few words.\n"Both patient and selfless, you have earned my treasure".\nInside are treasures untold, more than enough to share. You win!')
      else:
        print("Impatient to wait, you open the box excitedly. Your vision goes dark, and you go deaf in both ears. \nYou are consumed in a void of darkness, doomed never to escape the abyss. Game Over.")
    else:
      print("You walk over to the campsite. You are surprised to find a large tourist group! \nThey are sharing a large meal when they spot you. \nYou are invited over to eat and drink, and quickly make friends with the group. \nYou get lost in conversation, and forget why you came to the island in the first place. \nEventually, you leave the island together with your new friends, happy, full, and a little drunk. \nGame Over?")
  else:
    print("You are caught in a rip tide and are unable to resurface. Game Over.")
else:
  print("You fell into a hole. Game Over.")

  #Simple text adventure game
  #Not much effort into creating a storyline, really just nailing the
  #process of creating the scenario with nested statements