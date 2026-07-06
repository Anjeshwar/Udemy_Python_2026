# conditional statements - if, elif, else
'''
friend_name = "Anjesh"
user_name = input("Enter your name:")

if user_name == friend_name:
    print("Hello ", user_name)
    print("Glad to meet you!!")
else:
    print("Enter a valid username")
    
print("Thank you...")


print("\n----------------------------\n")

# checking the item/element present in a list
family = ["Anjesh", "Mohan", "Sai"]
friends = ["Ram", "Hanuma", "Krishna", "Shiva"]

member_name = input("Please enter your name: ")

if member_name in family:
    print("Hello, Family!")
elif member_name in friends:
    print("Hello, Friend!!")
else:
    print("I don't know you...")

print("\n----------------------------\n")

'''    

# Loops - While loop, for loop

# while loop - repeating undefined number of times
is_learning = True

while is_learning:
    print("You're Learning!!")
    is_learning = False
    
# Repeating the program until the condition gets false
user_input = input("Do you wish to run the program (Yes/No): ")

while user_input == "Yes":
    print("Program is running!!")
    user_input = input("Do you wish to run the program (Yes/No): ")
print("Program stopped...")


print("\n---------------\n")

# for loop - repeating defined number of times / repeating something certain number of times
animals = ['Lion', 'Tiger', 'Elephant', 'Wolf']
for animal in animals:
    print(animal)
    
for index in range(10):     # numbers from 0-9 - index values in range
    print(index)
    
print("\n")
    
for numbers in range(5, 10): # in between numbers including starting element
    print(numbers)

print("\n")

for num in range(0, 10, 3):  # in between element skipping 3 elements / every 3rd element including first element
    print(num)

print("\n")

# filtering names and score of students from list of dictionaries
students = [
    {"name":"Anjesh", "marks":99},
    {"name":"Mac", "marks":100},
    {"name":"Chary", "marks":91}
]

for student in students:
    print(student)
    
for student in students:
    st_namename = student["name"]
    print(st_namename)
    
for student in students:
    st_name = student["name"]
    st_marks = student["marks"]
    print(f'{st_name} scored {st_marks} marks')
    
print("\n")

