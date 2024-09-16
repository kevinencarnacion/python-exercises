#Write your code below this row 👇

for elements in range(1, 101):
  if elements % 3 == 0 and elements % 5 == 0:
    elements = "FizzBuzz"
  elif elements % 3 == 0:
    elements = "Fizz"
  elif elements % 5 == 0:
    elements = "Buzz"
  print(elements)
  
