#Operators

#Do these two programs.
# Practice 1: Ask the user for a whole number. 
# Print Even number or Odd number. 
# Use % and == inside an if / else.

num = int(input("Enter an integer: "))
if(num % 2 == 0):
    print("even")
else:
    print("Odd")


# Practice 2: Ask the user for two numbers. 
# Print the result of all seven arithmetic operators on them,with a clear label, like Add: 22.
print("Enter 2 Number: ")
num1 = int(input("1. "))
num2 = int(input("2. "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
if(num2 != 0):
    print("Devision:", num1 / num2)
    print("floor Devision:", num1//num2 )
    print("Modulas:", num1 % num2)
else:
    print("Error!")

print("Power:", num1**num2)