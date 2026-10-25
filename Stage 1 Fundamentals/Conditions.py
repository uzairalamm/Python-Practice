#conditions

age = int(input("Enter Your Age: "))
if age >= 18: print("Adult")
else: print("Teen")

# now lets use logical operators
# Check if a person can get a driving license
age = int(input("Enter Your Age: "))
hasId = input("Do you have an ID? (yes/no): ").lower()
if hasId == "yes" and age >=18:
    print("You can apply for a license.")
else:
    print("You cannot apply yet.")


# Practice 1: Ask the user for a number. 
# Print Positive, Negative or Zero.
num = int(input("Enter a Number: "))
if num > 0: print("Positive")
elif num < 0: print("Negative")
else: print("Zero")

# Practice 2: 
# ask for a year and print Leap year or Not a leap year.
# Rule: a year is a leap year if it is divisible by 4, except years divisible by 100, 
# which are not leap years, unless they are also divisible by 400. 
# (So 2000 is a leap year, 1900 is not, 2024 is.)
year = int(input("Enter a Year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Lear Year")
else:
    print("not a Leap Year")

# Practice 3: Ask for a user’s age and whether they have a ticket (yes/no). 
# Allow entry only if the age is 12 or more and they have a ticket. 
# Print a clear message for each case.

age = int(input("Enter Your Age: "))
hasTicket = input("Do You have Ticket(yes/no): ").strip().lower() #.strip() removes extra spaces around the answer,
if age >=12 and hasTicket == "yes":
    print("You can enter")
else:
    print("You can't enter")