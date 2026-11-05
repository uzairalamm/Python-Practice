Student = {
    "name": "Uzair",
    "age": 22,
    "email": "ualam4050@gmail.com"
}

name, age, email = Student.values()
print(name, age, email)

#how to access values in dictionary
print(Student["name"])
print(Student["age"])
print(Student.get("email")) # this is the same as student[key], but it doesn't raise any error, if key not found, it return none
print(Student.get("Aaaa", "Aaaa not found")) #if we didn't find the key, we return a default value 


#we can also add new key value pair
Student["city"] = "Lahore"

print("-------------------------------------------------------")
#Looping through dictionary
for key in Student:
    print(key, ":", Student.get(key))

print("-------------------------------------------------------")
for value in Student.values():
    print(value)

print("-------------------------------------------------------")
for key, value in Student.items():
    print(key, ":", value)

print("-------------------------------------------------------")


# A very common use: counting
word = "BAnana"
count = {}
for letter in word:
    letter = letter.lower()
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
print(count)


#length
print(len(Student))
print(Student.get("city"))

Student.pop("city") #this will remove the key value pair from dictionary
print(Student)

del Student["age"]
print(Student)


# Your turn (practice)
# Practice 1 (tuples): Make a tuple of the 7 days of the week. Print the first day, the last day, and the length. 
# Then print only the weekend days using a slice. 
# After that, write a function getMinMax(numbers) that returns the smallest and biggest number as a tuple.
# Call it and unpack the result into two variables.

weekend = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
print(weekend[0])
print(weekend[-1])
print(len(weekend))
print(weekend[5:])

def getMinMax(numbers):
    return min(numbers), max(numbers)

numbers = (1,23,4, 12, 44)
min, max = getMinMax(numbers)
print(min, max)



# Practice 2 (dictionary basics): Make a dictionary for a student with name, age, course and gpa. 
# Print the name. Then add a city, change the age, and remove the gpa. 
# Finally loop through the dictionary and print every key and value like name: Ali.

Student = {
    "name": "Uzair",
    "age": 22,
    "course": "Software Engineering",
    "gpa": 3.12
}
print(Student.get("name"))

Student["city"] = "Lahore"
Student["age"] = 21
Student.pop("gpa")
for key,value in Student.items():
    print(key, ":", value)



# Practice 3 (counting): Ask the user to type a word or sentence. 
# Count how many times each letter appears using a dictionary, 
# then print each letter and its count.
userInput = input("Enter a word or sentence: ")
charCount = {}

for letter in userInput:
    letter = letter.lower()
    if letter != ' ':
        if letter in charCount:
            charCount[letter] += 1
        else:
            charCount[letter] = 1
print(charCount)

# Practice 4 (phone book mini project): Make a phone book using a dictionary, 
# where the name is the key and the number is the value. 
# Use a while loop with this menu: 
# 1. Add contact, 
# 2. Search contact, 
# 3. Show all contacts, 
# 4. Exit. For search, 
# print Contact not found if the name does not exist. Use functions where it makes sense.




def addContact(phoneBook, name, number):
    phoneBook[name] = number

def searchContact(phoneBook, name):
    if name in phoneBook:
        return True
    return False

phoneBook = {}
while True:
    print("-------------------- Phone Book -------------------------")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. exit")
    choice = input("Enter Your Choice: ")

    if choice == '1':
        name = input("Enter the Name: ")
        number = input("Enter the Number: ")
        addContact(phoneBook, name, number)
        print("Contact Added to the PhoneBook")

    elif choice == '2':
        name = input("Enter the Name: ")
        if(searchContact(phoneBook, name)):
            print("Found")
        else:
            print("Not Found")

    elif choice == '3':
        print(phoneBook)

    elif choice == '4':
        print("exiting..........")
        break
    else:
        print("Invalid Choice")
