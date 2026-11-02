fruits = ["apple", "banana"]
print(fruits)

#insertion
fruits.append("Kiwi")
print(fruits)

fruits.insert(4, "mango")
print(fruits)
fruits.insert(5, "pista")
print(fruits[1:5]) #count first 1:5, but not 5, so it will be 1,2,3,4 index only

fruits.extend(["grapes", "orange", "Kiwi"]) # this will add multiple elements to the list at once at end
print(fruits)




#deletion
fruits.remove("Kiwi") # this will remove the first occurrence of the element
print(fruits)

fruits.pop() #this will remove last element
print(fruits)

#we can also use pop, and give it index to remove that element
fruits.pop(0) #this will remove the first element
print(fruits)

del fruits[1] # this will remove the second element
print(fruits)


#use full methods
marks = [12, 10, 10, 41, 33, 10]
print(max(marks))
print(min(marks))
print(sum(marks))
print(len(marks))
print(marks.index(41))
print(marks.count(10))

#sorting
marks.sort()
print(marks)
marks.reverse()
print(marks)

newMarks = list(sorted(marks))
print(newMarks)



marks = [12, 15, 8, 9]
#how to iterate list
len_marks = len(marks)
for i in range(len_marks):
    if i <len_marks - 1:
        print(marks[i], end=" -> ")
    else:
        print(marks[i])

#Or
for mark in marks:
    if mark != marks[-1]: # this mean if mark not equal to last element of the list
        print(mark, end=" -> ")
    else:
        print(mark)

# lets learn about its index
print("Index of each element:")
print(marks[3], end=" ")
print(marks[2], end=" ")
print(marks[1], end=" ")
print(marks[0], end=" ")
print(marks[-1], end=" ")
print(marks[-2], end=" ")
print(marks[-3] )

#reverse order
for i in range(len_marks):
    print(marks[-i-1], end=" ")