#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# password = ""
#We declare a variable to add characters later

#For each element in the range, which is defined by the user input
#we add to the base variable a random element from the given list

# for char in range(1, nr_letters +1):
#   password += random.choice(letters)
# for char in range(1, nr_symbols +1):
#   password += random.choice(symbols)
# for char in range(1, nr_numbers +1):
#   password += random.choice(numbers)

# print(password)



#For this easy level, the characters/symbols/numbers generated
#can be added sequentially


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#We must create a list so that we may make use of the random.shuffle function
#which would not function with just having a variable containing the elements
password_list = []

#Append vs +=/ the functionality is the same, it is just a different way of
#wording the calculation

for char in range(1, nr_letters +1):
  password_list.append(random.choice(letters))
for char in range(1, nr_symbols +1):
  password_list += random.choice(symbols)
for char in range(1, nr_numbers +1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

#As the list is correctly shuffled now, we must put it into a single variable so
#that when it is printed, it is not printed separately, but as a single phrase
password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")