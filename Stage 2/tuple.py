weekend = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
print(weekend[0:3])

#functions that works the same for list and tuple
numbers = (72, 33, 11, 22,45)
print(numbers[0:3])
print(numbers[0])
print(numbers[:4])
print(numbers[::2])
print(numbers[::-1])
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


#things that not works for tuple
# numbers[0] = 100  # This would raise an error because tuples are immutable
#sort(numbers) this would raise an error



#unpacking tuple
num1, num2, num3 = numbers[0:3]
print(num1)
print(num2)
print(num3)

#returning multiple values from a function
def minMax(numbers):
    return min(numbers), max(numbers)

min, max = minMax(numbers)
print(min, max)


numbers = [1, 2, 3]
numbersTuple = tuple(numbers)     # list to tuple
numbersList = list(numbersTuple)  # tuple to list