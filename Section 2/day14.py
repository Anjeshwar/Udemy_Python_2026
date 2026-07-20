# Lambda functions, First-class functions

# Lambda Functions - provides more simplicity to code 
add = lambda x, y: x+y      # variable = lambda inputs: returning value(output)

print(add(10, 20))      # x=10, y=20

print("\n")


average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Anj", "marks":(99, 97, 79, 100, 91, 90)},
    {"name": "Mac", "marks":(91, 77, 99, 93, 100, 88)},
    {"name": "Chary", "marks":(100, 99, 99, 96, 100, 97)}
]

for student in students:
    print(average(student["marks"]))
    
    
print("\n------------\n")

# -------------------------------------------

# First-class functions:
def greet():
    print("Hello, Anjesh!!!")
    
greet_anj = greet       # assigning function into a variable without brackets and calling the variable as a function.
greet_anj()

# -------------------------------

print()


avg = lambda seq: sum(seq) / len(seq)       # instead of functions using lambda functions
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    "average": avg,
    "total": total,
    "highest": top
}

Students = [
    {"name": "Anj", "marks":(99, 97, 79, 100, 91, 90)},
    {"name": "Mac", "marks":(91, 77, 99, 93, 100, 88)},
    {"name": "Chary", "marks":(100, 99, 99, 96, 100, 97)}
]

for student in Students:
    name = student["name"]
    marks = student["marks"]
    
    print()
    operation = input("Enter 'average'/ 'total'/ 'highest': ")
    
    operation_function = operations[operation]
    print(f"{name} got {operation} of {operation_function(marks)} marks")
    
