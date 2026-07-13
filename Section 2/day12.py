# Functions
def greet():        # defining the function
    user_input  = input("Enter your name: ")
    print(f"Hello, {user_input}")
    
greet()     # function calling

print("\n")

def user_details():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_designation = input("Enter your designation: ")
    user_exp = int(input("Enter your overall experience: "))
    
    print(f"Hii, {user_name}, You are {user_age} years old \n You have an experince of {user_exp} years in {user_designation} role..")
    
user_details()

print("\n--------------\n")

# Arguments & Parameters
def cars(fav_car):      # parameter - fav_car
    print(f"My favourite car is {fav_car}")
    
cars("Ferrari")     # argument - Ferrari

print("\n")

# --------------------------------

def myDetails(myName, myAge):
    print(f"My name is {myName} and I am {myAge}")
    
myDetails("Anjesh", 25)

#----------------------------------

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
def myDetails(name, age):
    print(f"Your name is {name} and you're {age}")
    
myDetails(user_name, user_age)

print("\n---------------------\n")

#--------------------------------------

bikes = [
    {
        "name": "Kawasaki Zx10r",
        "model": 2024,
        "tank": 18,
        "engine": "1000cc",
        "maxSpeed": 370,
        "distance": 280,
        "fuelConsumed": 14
    },
    {
        "name": "Pulsar 220f",
        "model": 2022,
        "tank": 14,
        "engine": "220cc",
        "maxSpeed": 145,
        "distance": 600,
        "fuelConsumed": 15
    },
    {
        "name": "Royal Enfield 350",
        "model": 2025,
        "tank": 15,
        "engine": "350cc",
        "maxSpeed": 160,
        "distance": 840,
        "fuelConsumed": 21
    }
]

def bike_capacity(bike):        
    kmpl = bike["distance"] / bike["fuelConsumed"]
    mileagePerFulltank = kmpl * bike["tank"]

    print(f"{bike['name']} gives {kmpl:.2f} km/L")
    print(f"It can go up to {mileagePerFulltank:.2f} km with its full tank.")

bike_capacity(bikes[1])     # calling the function by passing an argument

print("\n")

for bike in bikes:
    bike_capacity(bike)


