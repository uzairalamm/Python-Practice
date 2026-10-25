# Datatypes
int, float, str, bool 

#Asking python datatype of variables
#we use type() function

fName = "Uziar"
lName = "Alam"
roll = 52
age = 22
isStudent = True;

print(type(fName))
print(type(roll))
print(type(age))
print(type(isStudent))

print(fName + ' ' + lName) #concatenation

#Now lets move to the good part..
#lets take userInput

name = input("Enter Your Name: ")
print("hello ", name , "Your are ", age, "years old")
#by defualt input function make everything string
#let me give you an example

num1 = input("Enter Num1: ") #2
num2 = input("Enter Num2: ") #4
print(num1 + num2) #guess the input? you think it should be 6 right, but no, its 24 

#To make it right we mention datatype with input function
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
print(num1 + num2)