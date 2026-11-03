#print Hello World
def printHello():
    print("Hello, World!")

#function Intialization
def addNumbers(num1, num2):
    return num1 + num2

#even odd



printHello()
print(addNumbers(5,10))



#Practice 1: Write a function squareNumber(number) that returns the square of a number. 
# Ask the user for a number, call the function, and print the result.
def squareNumber(number):
    return number * number

# ask the userInput
userInput = int(input("Enter a Number: "))
print(f"the square of {userInput} = {squareNumber(userInput)}")

# Practice 2: Write a function isEven(number) that returns True or False. 
# Use it inside an if/else to print Even number or Odd number.
def isEven(num):
    if num % 2 == 0:
        return True;
    return False;
print(isEven(4))
print(isEven(5))


# Practice 3: Write a function calculateTotal(price, quantity, discount=0) that returns the total cost 
# after taking off the discount percentage. 
# For example, price 200, quantity 3, discount 10 gives 540. 
# Call it once with a discount and once without.
def calculateTotal(price, quantity, discount=0):
    total = price * quantity
    discount = total * (discount/100)
    return total - discount
  

print(f"Without Discount: {calculateTotal(200,3,0)}")
print(f"With Discount: {calculateTotal(200,3,10)}")



# Practice 4 (Stage 1 mini project, the simple calculator): Make a calculator using everything from Stage 1.
# Write four functions: addNumbers, subtractNumbers, multiplyNumbers and divideNumbers (the last one must handle division by zero).
# Use a while loop to show a menu: 1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exit.
# Ask for the choice, then ask for two numbers, call the right function and print the answer.
# Keep going until the user picks 5. Print Invalid choice for any other number.

def addNumbers(num1, num2):
    return num1 + num2

def subtractNumbers(num1,num2):
    return num1 - num2

def multiplyNumbers(num1,num2):
    return num1 * num2

def divideNumbers(num1,num2):
    if num2 != 0:
        return num1/num2;
    return "Error! Division by Zero"

while True:
    print("\n============ Simple Calculator ==============")
    print("1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. Exit")
    choice = int(input("Enter your Choice: "))
    if choice == 5:
        break
    elif choice <1 or choice >5:
        print("Invalid Choice")
        continue
    num1 = int(input("Enter Num1: "))
    num2 = int(input("Enter Num2: "))

    if choice == 1:
        print(addNumbers(num1, num2))
    elif choice == 2:
        print(subtractNumbers(num1, num2))
    elif choice == 3:
        print(multiplyNumbers(num1, num2))
    elif choice == 4:
        print(divideNumbers(num1, num2))

    
print("Bye........................")