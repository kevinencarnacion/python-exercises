# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#We make all string input lowercase so that it can be checked against 'true love'
name1_lower = name1.lower()
name2_lower = name2.lower()

#We create a larger variable to store the number of times both names
#contain characters found in the word true
true_score = name1_lower.count('t')
true_score += name1_lower.count('r')
true_score += name1_lower.count('u')
true_score += name1_lower.count('e')
true_score += name2_lower.count('t')
true_score += name2_lower.count('r')
true_score += name2_lower.count('u')
true_score += name2_lower.count('e')

#We do the same as above, this time for the word love
love_score = name1_lower.count('l')
love_score += name1_lower.count('o')
love_score += name1_lower.count('v')
love_score += name1_lower.count('e')
love_score += name2_lower.count('l')
love_score += name2_lower.count('o')
love_score += name2_lower.count('v')
love_score += name2_lower.count('e')

#If left as integers, they will be added together instead of being concatenated
#So they are converted to strings for output
final_score = str(true_score) + str(love_score)

#We want the score as integers so that they can be calculated within
#the margins of the calculator
if int(final_score) <= 10 or int(final_score) >= 90:
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif int(final_score) >= 40 and int(final_score) <= 50:
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")

#This was my solution, though again, not reduced/efficient in terms of lines used
#Below is the solution provided by the instructor

combined_string = name1 + name2
lower_case_string = combined_string.lower

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

#Everything is mostly the same for printing, with some minor changes
#This is far neater, and in this case, I think much more legible than my code

#To note; this is a very complex way of determining a number that could ultimately be decided with a random pull from a specified range. In this case, likely 0-100.