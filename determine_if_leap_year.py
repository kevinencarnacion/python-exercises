# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#This was my solution
#Though it works, and logically I followed the same steps
#The solution is not as clean as it could be, especially
#Since there is a conditional without an action - to avoid double printing
#the same message
if year % 4:
  print ("This year is NOT a leap year")
  if year % 100:
    year
  elif year % 400:
    print ("This year is NOT a leap year")
  else:
    print ("This year is a leap year")
else:
  print ("This year is a leap year")


#This is cleaner, instructor provided solution

#I thought of writing it this way, but in terms of my own understanding
#I understood that the system was checking that value
#Writing it out this way just makes it more legible
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

#I much prefer this second solution, as it is much more legible
#and easier to track all around
#I was on track to get this solution, though worded differently
#but I was determined to make it work with an elif statement
#Moving forward, I will remember the process here and hopefully
#apply it to my work in the future