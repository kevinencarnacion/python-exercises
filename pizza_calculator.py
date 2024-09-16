# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#bill is declared so it can be used later
bill = 0

#Since size input determines cost, we assign values to size
#based on the string input
if size == "S":
  size = 15
  if add_pepperoni == "Y":
    size += 2
elif size == "M":
  size = 20
  if add_pepperoni == "Y":
    size += 3
else:
  size = 25
  if add_pepperoni =="Y":
    size += 3
if extra_cheese == "Y":
  size += 1
#The code here only checks for sizes on Small and Medium
#Thus, any letter typed outside of S and M will be considered
#a large size pizza in the calculations

bill = size

print(f"Your final bill is: ${bill}")

#This was my solution
#Below is a cleaner way of writing the same function
  

if size == "S":
  size = 15
elif size == "M":
  size = 20
else:
  size = 25
if add_pepperoni =="Y":
    if size == "S":
      bill += 2
    else:
      bill += 3
if extra_cheese == "Y":
  size += 1

#I recognized when making my code that there was redundancy
#in repeated the add_pepperoni lines to the individual sizes
#but it worked for me logically to think it through in that manner
#In other words, I recognized that I could make code as in this above
#example; but worked it through my way first; with the intent of moving after