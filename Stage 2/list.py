# fruits = ["apple", "banana"]
# print(fruits)

# #insertion
# fruits.append("Kiwi")
# print(fruits)

# fruits.insert(4, "mango")
# print(fruits)
# fruits.insert(5, "pista")
# print(fruits[1:5]) #count first 1:5, but not 5, so it will be 1,2,3,4 index only

# fruits.extend(["grapes", "orange", "Kiwi"]) # this will add multiple elements to the list at once at end
# print(fruits)




# #deletion
# fruits.remove("Kiwi") # this will remove the first occurrence of the element
# print(fruits)

# fruits.pop() #this will remove last element
# print(fruits)

# #we can also use pop, and give it index to remove that element
# fruits.pop(0) #this will remove the first element
# print(fruits)

# del fruits[1] # this will remove the second element
# print(fruits)
# fruites.clear()


# #use full methods
# marks = [12, 10, 10, 41, 33, 10]
# print(max(marks))
# print(min(marks))
# print(sum(marks))
# print(len(marks))
# print(marks.index(41))
# print(marks.count(10))

# #sorting
# marks.sort()
# print(marks)
# marks.reverse()
# print(marks)

# newMarks = list(sorted(marks))
# print(newMarks)


# access list element.
# print(marks[0:])
# print(marks[:1])
# print(marks[::2])
# print(marks[::-1]) # reverse order


# marks = [12, 15, 8, 9]
# #how to iterate list
# len_marks = len(marks)
# for i in range(len_marks):
#     if i <len_marks - 1:
#         print(marks[i], end=" -> ")
#     else:
#         print(marks[i])

# #Or
# for mark in marks:
#     if mark != marks[-1]: # this mean if mark not equal to last element of the list
#         print(mark, end=" -> ")
#     else:
#         print(mark)

# # lets learn about its index
# print("Index of each element:")
# print(marks[3], end=" ")
# print(marks[2], end=" ")
# print(marks[1], end=" ")
# print(marks[0], end=" ")
# print(marks[-1], end=" ")
# print(marks[-2], end=" ")
# print(marks[-3] )

# #reverse order
# for i in range(len_marks):
#     print(marks[-i-1], end=" ")


#Practice 1: Make a list of 5 fruits. Print the first item, the last item, and the length. 
# Then add one fruit at the end, remove one fruit, and print the final list.
fruits = ["apple", "banana", "mango", "grapes", "kiwi"]
print(f"First Fruit: {fruits[0]}")
print(f"Last Fruit: {fruits[-1]}")
print(f"length Fruit: {len(fruits)}")


# Practice 2: Ask the user for 5 numbers and store them in a list. 
# Print the list, the total, the average, the biggest, the smallest, 
# and the list sorted from smallest to biggest.
marks = [20, 90, 11, 23, 12]
print(marks)
print(f"sum: {sum(marks)}")
avg = sum(marks)/len(marks)
print(f"average: {avg}")
print(f"biggest: {max(marks)}")
print(f"smallest: {min(marks)}")
print(f"Sorted: {sorted(marks)}")

# Practice 3: Take the marks [45, 78, 32, 91, 60, 38]. 
# Using a loop, count how many students passed (40 or more) and 
# how many failed, and print both counts.
newMarks = [45, 78, 32, 91, 60, 38]
passCount = 0
failCount = 0
for i in range(len(newMarks)):
    if newMarks[i] >= 40:
        passCount +=1
    else:
        failCount +=1

print(f"Pass: {passCount}")
print(f"Fail: {failCount}")

# Practice 4: Take the list [1, 2, 2, 3, 3, 3, 4]. 
# Make a new list that has each number only once (no repeats). 
# Use a for loop and the in operator.
mylist = [1, 2, 2, 3, 3, 3, 4]
newList = []
for i in range (len(mylist)):
    if mylist[i] not in newList:
        newList.append(mylist[i])
print(newList)