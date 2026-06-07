# Strings
my_name = "Anjeshwara chary"
designation = 'Software Engineer - Research & Development'
print(my_name)
print(designation)

quote = "Hey, Wts'up"
print(quote)

# Escaping
quote2 = "He said \"You are Amazing\" Yesterday."       # back slash before inside quotes
print(quote2)

multiline = """Hey, Hi!!
How do you do??
All good...
"""
print(multiline)

print()

name = "Anjesh"
greet = "Congratulations!! "+ name
print(greet)

my_age = 25
num_into_string = str(my_age)
print(my_age, type(my_age))
print(num_into_string, type(num_into_string))

print()

# String Formatting - f strings
age = 24
print(f'You are {age}')

name = "Anjesh"
greeting = f"How are you {name}?"
print(greeting)

name2 = "Mac"
print(greeting)     # here it will not replace "Anjesh with Mac"

name3 = "Chary"
greetings = "How are you {}?"
greet_name3 = greetings.format(name3)     # .format() replaces {} with the passed variable into it
print(greet_name3)


greet_name4 = greetings.format("MAC")      # here it will replace the Chary with MAC.
print(greet_name4)

print("\n-------------\n")

# User input
user_name = input("Enter your name: ")
print(user_name)

user_age = int(input("Enter your age: "))
print(f'Your name is {user_name}, You are {user_age}\n')

user_age2 = input("Enter your age: ")
print(f"You have lived for {user_age2 * 12} months")    # here the input is a string.
print(f"You have lived for {int(user_age2) * 12} months\n") 

# Booleans
