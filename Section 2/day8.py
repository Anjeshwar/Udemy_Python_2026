# Coding challenge - Fizz Buzz
for num in range(1, 101):
    if num%3 == 0 and num%5 == 0:
        print("FizzBuzz")
    elif num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)

print("\n")
        
# Loops with else statement
cars = ["ok", "ok", "ok", "ok", "ok"]
for status in cars:
    if status == "faulty":
        print("Found a faulty car, stopped production...")
        break
    print(f"This car is {status}")
else:
    print("All cars built successfully")
    
print("\n")

# prime numbers - finding prime & composite numbers
for n in range(2, 10):
    for x in range(2, n):
        if n%x == 0:
            print(f"{n} is a composite number")
            break
    else:
        print(f"{n} is a prime number")
        
print("\n")

# printing prime numbers in a range
for n in range(2, 20):
    for x in range(2, n):
        if n%x == 0:
            break
    else:
        print(n)
        
print("\n")

# checking the given number is prime or not
user_input = int(input("Enter any number: "))
for n in range(2, user_input):
    if user_input%n == 0:
        print(f"{user_input} is a composite number")
        break
else:
    print(f"{user_input} is a prime number")

print("Done for the day")