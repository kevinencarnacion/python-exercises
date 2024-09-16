#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

#Calculator to determine tip amount based off inputs given
print("Welcome to the tip calculator.")
bill_amount = input("What was the total bill? $")
people_amount = input("How many people to split the bill? ")
tip_percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

#A new variable is called to pass the tip_percentage input as an integer
tip_int = int(tip_percentage)
#called_tip is the method to calculate the tip percentage
called_tip = tip_int * .01 + 1

#bill_total calculates the correct tip amount based on input values by
#dividing the flat bill amount by the amount of people splitting the bill
#and lastly multiplying that number by the tip percentage
bill_total = float(bill_amount) / int(people_amount) * called_tip

#To both round off the float at 2 decimals, and cap it at 2 decimals
#a new variable is called to establish the rules for the float
rounded_total = round(bill_total, 2)
#str.format(*args) is used here to establish the float as a string
#to ensure that 2 decimal values are always shown
#{.2f} is used to determine 2 decimal values on the float value
rounded_total = "{:.2f}".format(bill_total)
print(f"Each person should pay: ${rounded_total}")