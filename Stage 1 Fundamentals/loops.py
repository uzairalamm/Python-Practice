#loops
count = 1
while count <= 5:
    print(count, end=' ')
    count+=1
print()

# Print numbers from 1 to 5 using for loop
for i in range(1,6):
    print(i)


# Print each letter of a word on its own line
word = "Hello"
for char in word:
    print(char)


# Add all numbers from 1 to 10
sum = 0
for num in range(2,11):
    sum +=num
print(sum)



# Print the table of a number
num = int(input("Enter a Number: "))
print(f"Table of {num}")
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")



# Practice 1: Print the numbers 1 to 10 using a for loop. 
for num in range(1,11):
    print(num, end= " ")
print()

# Then print 10 down to 1 using a while loop.
count = 10
while count > 0:
    print(count, end= " ")
    count -=1
print()

# Practice 2: Ask the user for a number and print 
# its multiplication table up to 10 using f-strings.

# Practice 3: Find the sum of all even numbers from 1 to 100 and print it. 
# (Use for, % and a total variable.)

# Practice 4: Make a number guessing game. Keep a secret number (for example 7). 
# Keep asking the user to guess until they get it right. 
# After each wrong guess, print Too high or Too low. At the end, 
# print how many attempts it took. (Use while, if/elif, and a counter.
# A boolean flag is a good idea here.)




# Keep asking until the user enters the correct password
correctPassword = "123456"
print("Enter Password:", end=' ')
count = 0
while True:
    enteredPassword = input()
    if(enteredPassword !=correctPassword):  
        count+=1  
        if count >= 3:
            print("You have Reached Your Limit")
            break
        print("Wrong! Enter Again:", end= ' ')
    else:
        print("Password Correct")
        break

    
if count < 3:
    print("Access granted.")

