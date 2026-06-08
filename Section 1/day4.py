# Lists
friends = ["Anjesh", "Sai", "Mohan"]
print(friends)
print(type(friends))

print("-----------\n")

# Retrieving the elements from list using "Indexes"
print(friends[0])       # to get first element - Anjesh
print(friends[1])       # to get second element - Sai
print(friends[2])       # to get third element - Mohan

# Length of list - to find number of elements present in the list
print(len(friends))

print("----------------\n")

# Lists inside lists
friendsWithAges = [["Anjesh", 25], ["Mohan", 49], ["Sai", 24]]
print(friendsWithAges)
print(friendsWithAges[0])
print(friendsWithAges[0][0])
print(friendsWithAges[1][0])
print(friendsWithAges[1][1])
print(friendsWithAges[2][1])

all_friends = [
    ["Anj", 25],
    ["Mohan", 49],
    ["Sai", 24],
    ["Mac", 24],
    ["Chary", 25]
]
print(all_friends)

print("----------------\n")

myFriends = ["Anj", "Mohan", "Sai"]     # Adding elements into a list - append
print(myFriends)
myFriends.append("Mac")     # adding "Mac" to the list
print(myFriends)

myFriends.remove("Anj")     # Removing elements from the list - remove
print(myFriends)

print("\n-------------\n-------------\n")

# Tuples - we cannot add and remove elements as in lists - Unchanged
bikes = ("220f", "Zx10r", "H2r")
print(bikes, type(bikes))

bikes = bikes + ("R15",)    # we can add using concatenation but not with append like in lists
print(bikes)

print("\n-------------\n-------------\n")

# Sets - no order, no duplicates
RichEndCars = {"Audi", "BMW", "Mercedes", "Toyota"}
NormalCars = {"Tata", "Toyota", "Suzuki", "Hyundai"}

RichEndCars.add("Ferrari")      # to add elements into set - add()
print(RichEndCars)

NormalCars.remove("Tata")       # to remove elements from set - remove()
print(NormalCars)

rich_but_not_normal = RichEndCars.difference(NormalCars)    # gives the elements which are in one set not in another set
print(rich_but_not_normal)

normal_but_not_rich = NormalCars.difference(RichEndCars)
print(normal_but_not_rich)

in_both = RichEndCars.intersection(NormalCars)              # gives the elements which are in both the sets
print(in_both)

not_in_both = RichEndCars.symmetric_difference(NormalCars)  # gives the elements which are not in both the sets
print(not_in_both)

allCars = RichEndCars.union(NormalCars)                     # give both the sets without duplicates
print(allCars)


