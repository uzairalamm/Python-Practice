#loops

# count = 1
# while count <= 5:
#     print(count, end=' ')
#     count+=1

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