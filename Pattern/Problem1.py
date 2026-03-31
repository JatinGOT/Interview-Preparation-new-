# Write a Python program that:

# Takes a number n

# Prints numbers from 1 to n

# For each number:

# If the number is divisible by both 3 and 5, print "FizzBuzz"

# If divisible by only 3, print "Fizz"

# If divisible by only 5, print "Buzz"

# Otherwise, print the number itself
while True:
    user_input = input("Enter a number (press q to exit): ")

    if user_input == 'q':
        print("Loop exited")
        break

    try:
        num = int(user_input)
        for i in range(1, num + 1):
                    if i % 3 == 0 and i % 5 == 0:
                        print("FizzBuzz")
                    elif i % 3 == 0:
                        print("Fizz")
                    elif i % 5 == 0:
                        print("Buzz")
                    else:
                        print(i)
    except ValueError:
            print("Data Type Error")