# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#print(student_heights)


total_height = 0
#For each instance of an element, heights in this example
#Add each element into itself to arrive at a sum total
for heights in student_heights:
  total_height += heights
#print(total_height)

number_of_students = 0
#For each instance of an element in the list, labeled students here
#Add 1 to the variable number_of_students which was defined as 0 initially
for students in student_heights:
  number_of_students += 1
#print(number_of_students)

#Calculate the average, making sure to round the number to avoid decimals
average_height = round(total_height / number_of_students)
print(f"The average height of those input is: {average_height}")