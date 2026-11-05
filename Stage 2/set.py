my_list = [1,2,2,2,2,3,4,11,1,1,12,3,4,5,6,7]
my_set = set(my_list)
print(my_set)

# Practice 1: Make a set of 5 numbers. Add one new number. 
# Try adding a number that is already there and see that nothing changes.
# Remove a number using discard. Print the set and its length.
new_set = {1,3,2,4,5,12}
new_set.add(11)
new_set.add(11)
print(new_set)
new_set.discard(11)
print(new_set)
print(len(new_set))




# Practice 2: Ask the user to type a sentence. 
# Use a set to print how many different letters it has, ignoring spaces and capital letters.
sentence = input("Enter a sentence: ")

set_sentence = set()
for letter in sentence:
    if letter.isupper() or letter == " ":
        continue
    set_sentence.add(letter)

print(set_sentence)

# Practice 3: Make two sets: students who play cricket and students who play football 
# (at least 4 names each, with some names in both). 
# Print who plays both, who plays at least one of the two, who plays only cricket, 
# and who plays exactly one of the two games.

criketPlayer = {"Ali", "Ahmed", "Usman", "Salman"}
footballPlayer = {"Ahmed", "Butt", "Umaid", "Ruman"}
print(f"who plays both FootBall and Criket: {(criketPlayer & footballPlayer)}")
print(f"who plays at least one of the two: {(criketPlayer | footballPlayer)}")
print(f"who plays only cricket: {(criketPlayer - footballPlayer)}")
print(f"who plays only football: {(footballPlayer - criketPlayer)}")
print(f"who plays exactly one of the two games: {(criketPlayer ^ footballPlayer)}")

# Practice 4: Take the list [5, 3, 5, 2, 3, 1, 2]. 
# Remove the duplicates using a set and print the unique numbers in order from smallest to biggest.

my_list = [5, 3, 5, 2, 3, 1, 2]
my_set = set(my_list)
print(my_set)