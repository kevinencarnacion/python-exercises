import random

#To use the random module in python, it must be imported first

#Created the list/array populated from 1-100
#I set the range as 0 - 101 to include the full range of 0-100
numbers_list = list(range(0, 101))
print(numbers_list)

#.pop is used to remove a specific element
#in this case, since we are removing it randomly
#we define the range it will be working with, which in this
#case we must utilize the len operator to draw the range from the generated list
random_element = numbers_list.pop(random.randrange(len(numbers_list)))

#Added this just to make the console easier to read
print("------------------------------------------------------------\n")

#As random_element was the assigned variable when calculating the
#element to be removed, I can then print that variable to determine
#which element was removed from the list


print(f"The number that was removed from the list is: {random_element}")

#Using the set method, the list is compared and checks for
#the difference, which is the used to determine any missing elements
removed_element = list(set(range(max(numbers_list) + 1)) - set(numbers_list))
print(f"The missing element is : {removed_element}")



#Simpler method to randomly remove the integer, since I have a defined list
#numbered_list = list(range(0, 101))
#removed_number = numbered_list.pop(random.randint(0, 101))
#print(removed_number)

