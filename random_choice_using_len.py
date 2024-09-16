# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

#names variable takes a random name from the range of elements in the list
#print(names)

#names = names.pop(random.randrange(len(names)))
#print(f"{names} is going to pay the bill today!")

#This is a method I learned, which actually randomly removes the element from the list
#It works in this context, as I don't need to reprint the full list
#However, if there were more steps after which required the original list
#Then this method is flawed

#Below is the instructor provided method, which works in the context
#of keeping the list intact, and still having the same outcome

#Get the total number of items in list using len function
#num_items = len(names)

#random_choice = random.randint(0, num_items - 1)
#person_who_will_pay = names[random_choice]
#print(f"{person_who_will_pay} is going to buy the meal today!")


#Lastly, using the choice function below

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")
