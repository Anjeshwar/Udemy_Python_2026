# Set & Dictionary Comprehension, Zip function, Enumerate function

# Set Comprehension
friends = ["Anj", "Sai", "Mohan", "Krish"]
guests = ["Hanuma", "anj", "Mohan", "Ram"]

friends_lower = {f.lower() for f in friends}    # set comprehension
guests_lower = {g.lower() for g in guests}      # set comprehension

both = friends_lower.intersection(guests_lower)
both = {name.title() for name in both}          # set comprehension

print(both)     # output: {'Anj', 'Mohan'}

print("\n")


# Dictionary Comprehension
friends = ["Anj", "Sai", "Mohan", "Mac"]
last_seen = [0, 3, 1, 5]

long_timers = {
    friends[i] : last_seen[i]
    for i in range(len(friends))
}
print(long_timers)      # output: {'Anj': 0, 'Sai': 2, 'Mohan': 1}

print("\n")

long_timers = {
    friends[i] : last_seen[i]
    for i in range(len(friends))
    if last_seen[i] > 2
}
print(long_timers)      # output: {'Sai': 3, 'Mac': 5}


print("\n--------------\n")


# Zip Function
friends = ["Mac", "Chary", "Anju"]
last_seen = [3, 4, 7]

zipFn = zip(friends, last_seen)     # using zip function we are making the elements in both the list into tuples - [("Mac", 3), ("Chary", 4), ("Anju", 7)]
long_timers = dict(zipFn)           # using dict() converting tuples into dictionaries
print(long_timers)

print("\n")

# list of tuples using zip function
zip_lists = list(zip(friends, last_seen))   # output: [('Mac', 3), ('Chary', 4), ('Anju', 7)]
print(zip_lists)

zip_lists = list(zip(friends, last_seen, [1,2,3,4,5]))  # output: [('Mac', 3, 1), ('Chary', 4, 2), ('Anju', 7, 3)]
print(zip_lists)

print("\n--------------\n")


# enumerate function - joining the list with a number
bikes = ["Kawasaki Zx10r", "Pulsar 220f", "Royal Enfield"]

    # without enumerate
counter = 0
for bike in bikes:
    print(counter)
    print(bike)
    counter = counter + 1

print("\n")

    # with enumerate
for count, bike in enumerate(bikes):
    print(count)
    print(bike)
    
print("\n")  

for count, bike in enumerate(bikes, start=1):
    print(count)
    print(bike)

print("\n") 
  
    # enumerate with list 
print(list(enumerate(bikes)))
print(list(enumerate(bikes, start=2)))


    # enumerate with dict
print(dict(enumerate(bikes)))