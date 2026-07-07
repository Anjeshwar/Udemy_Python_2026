# List Slicing - [start:end]
friends = ["Anjesh", "Mohan", "Sai", "Mac", "Chary"]

print(friends[1:4])     # prints elements from indexes 1,2,3 not included 4
print(friends[:3])      # prints elements from 0th index to 3 excluding index 3
print(friends[2:])      # prints elements starting from index 2 to last index in list

print(friends[:])       # prints all the elements in a new list

print(friends[-3:])     # negative indexes will be counted from end of the list. It prints from negative indexed element to next elements
print(friends[-4:-2])   # prints elements from -4th index to -2th index excluding -2th index element
print(friends[-3:4])    # prints elements from -3rd index to 4h index excluding 4th indexed element
print(friends[:-2])     # prints elements from starting of list to -2 index element excluding it


print("\n--------------\n")

# List Comprehension

# Doubling numbers in a list without List Comprehension
numbers = [1,2,3,4,5]
doubled_nums = []

for num in numbers:
    doubled_nums.append(num*2)      # doubling the numbers and appending it to list
print(doubled_nums)

# doubling numbers in a list with List Comprehension
doubled_nums = [num*2 for num in numbers]   # List comprehension
print(doubled_nums)

# doubling numbers in a list with a range using list comprehension
doubled_nums = [num*2 for num in range(11)]
print(doubled_nums)

# printing strings in a list from another list
friends_ages = [25, 24, 29, 23]
age_strings = [f"My friend is {age} years old" for age in friends_ages]
print(age_strings)

print("\n")

# Converting the string elements in a list into upper or lower case
names = ["Mac", "Chary", "Anj"]
lowercase = [name.lower() for name in names]    # Lower Case
print(lowercase)

uppercase = [name.upper() for name in names]    # Upper Case
print(uppercase)

print("\n")

# comparing user element present in a list of elements with casing property
friend = input("Enter your name: ")
friends_list = ["Anj", "Sai", "Mohan", "Krish", "Hanuma"]
friends_list_lower = [name.lower() for name in friends_list]

if friend.lower() in friends_list_lower:
    print(f"{friend} is my friend")
else:
    print(f"{friend} is not my friend")
    
# title casing - .title() - it gives the title casing element what ever the input you give
if friend.lower() in friends_list_lower:
    print(f"{friend.title()} is my friend")
else:
    print(f"{friend.title()} is not my friend")
    
print("\n-----------------\n")


# Comprehensions with conditionals
ages = [21, 24, 25, 27, 26]
odd_ages = [age for age in ages if age%2 == 1] # printing ages in list with looping the ages then checking condition
print(odd_ages)

print("\n")

# checking similar elements in 2 seperate lists and printing - intersection()
friends = ["Anj", "Chary", "anju", "mac"]
relatives = ["chary", "Sai", "ANJ", "Mohan"]

friends_lower = set([f.lower() for f in friends])       # creating set
relatives_lower = set([r.lower() for r in relatives])   # creating set

print(friends_lower.intersection(relatives_lower))

# checking similar elements in 2 seperate lists and printing without creating sets
friends = ["Anj", "Chary", "anju", "mac"]
relatives = ["chary", "Sai", "ANJ", "Mohan"]

relatives_lower = [r.lower() for r in relatives]

frndCumRelative = [
    name 
    for name in friends 
    if name.lower() in relatives_lower
]
print(frndCumRelative)


