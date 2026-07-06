# Destructuring syntax
currencies = (0.8, 1.2)    # storing tuple elements in a variable
usd, eur = currencies       # Destructuring or storing elements in a tuple of stored variable into seperate variables

print(usd)
print(eur)

print("\n")

friends = [("Anjesh", 25), ("Mohan", 49), ("Sai", 24)]

for name, age in friends:
    print(f"{name} is {age} years old")
    
print("\n----------\n")


# Iterating over dictionaries
friends_ages = {"Anjesh":25, "Mohan":49, "Sai":24}  # Dictionary = Key:Value pair
Anjesh_age = friends_ages["Anjesh"]
print(Anjesh_age)

for name in friends_ages:   # It only gives the keys from the dictionary
    print(name)

for age in friends_ages.values():   # .values() gives the values in a dictionary
    print(age)

for name, age in friends_ages.items():  # in dictionaries, we need to use .items() to desturcture/ to iterate both key and value pair in dictionaries.
    print(f"{name} is {age} years old")
    

print("\n-----------\n")


# Break & Continue
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    print(f"This car is {status}")

print("\n")
    
for status in cars:
    if status == "faulty":
        print("Found a faulty car, stopped production...")
        break
    print(f"This car is {status}")
    
print("\n")

for status in cars:
    if status == "faulty":
        print("Found a faulty car, skipping it......")
        continue
    print(f"This car is {status}")
    print("Shipping new car to the customer")
    
print("\n")
print("Day 7 is completed...")
