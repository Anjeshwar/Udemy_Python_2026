# Intro to OOPs - Object Oriented Programming

# Syntax:
"""
class ClassName:
    # constructor
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # method
    def display(self):
        print(self.attribute1)
        print(self.attribute2)
"""

    # __init__ is a constructor method in Python.
    # It is a special method that runs automatically when an object is created.



class Student:
    def __init__(self, name, marks):                # __init__ is a constructor
        self.name = name
        self.marks = marks
        
    def average(self):                              # average() is called as a method here inside a class
        return sum(self.marks) / len(self.marks)

my_student = Student("Anjesh", [99, 97, 100, 89, 91])

print(my_student.name)              # printing student name
print(my_student.average())         # printing average marks of the student

print("\n")

student_one = Student("Anju", [100, 99, 91, 89, 100])
student_two = Student("Chary", [97, 69, 96, 88, 100])
student_three = Student("Mac", [100, 100, 97, 100, 94])

print(student_one.name)         # gives student one name
print(student_one.average())    # gives student one average marks
print(student_two.name)
print(student_two.average())
print(student_three.name)
print(student_three.average())


# ----------------------------------------------------------------



# Built-in Functions -> https://docs.python.org/3.7/library/functions.html
''' 
    abs(), delattr(), hash(), memoryview()
    set(), all(), dict(), help()
    min(), setattr(), any(), dir()
    hex(), next(), slice(), ascii()
    divmod(), id(), object(), sorted()
    bin(), enumerate(), input() oct()
    staticmethod(), bool(), eval(), int()
    open(), str(), breakpoint(), exec()
    isinstance(), ord(), sum(), bytearray()
    filter(), issubclass(), pow(), super()
    bytes(), float(), iter(), print()
    tuple(), callable(), format(), len()
    property(), type(), chr(), frozenset()
    list(), range(), vars(), classmethod()
    getattr(), locals(), repr(), zip()
    compile(), globals(), map(), reversed()
    __import__(), complex(), hasattr(),max(), round()
'''