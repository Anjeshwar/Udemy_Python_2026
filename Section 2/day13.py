# Functions & return values, Default parameter values

# Return - once we use return keyword, the next set of lines in the function will not execute and once we are returning the value it get store in the funtion and not get printed. we have to print it in another function or outside the function
bikes = [
    {"name": "Kawasaki Zx10r", "tank": 18, "distance": 280, "fuelConsumed": 14},
    {"name": "Pulsar 220f", "tank": 14, "distance": 600,"fuelConsumed": 15},
    {"name": "Royal Enfield 350", "tank": 15, "distance": 840,"fuelConsumed": 21}
]

def bike_name(bike):
    return bike["name"]

def bike_capacity(bike):        
    kmpl = bike["distance"] / bike["fuelConsumed"]
    return kmpl


def mileage(bike):
    kmpl = bike_capacity(bike)
    mileagePerFulltank = kmpl * bike["tank"]
    return mileagePerFulltank


def bike_info(bike):
    name = bike_name(bike)
    bike_kmpl = bike_capacity(bike)
    bike_mileage = mileage(bike)
    
    print(f"{name} goes {bike_kmpl:.2f}km/l and can travel {bike_mileage:.2f} km on a full tank")


for bike in bikes:
    bike_info(bike)             # no need to print this function as all the things are printed in bike_info() function. If we are not printing there we can print here.


print("\n--------------------------------\n")

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

def divide(x, y):               # x, y are parameters which are receiving from function calling
    if y == 0:
        return "You can't divide a number by Zero"
    else:
        return x/y

print(divide(a, b))             # a&b are arguments passing to the function