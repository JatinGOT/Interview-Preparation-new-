while True:
    user_input = input("Enter a number (or 'q' to quit): ").lower()
    
    if user_input == 'q':
        break
    try:
        x = int(input("Enter a number "))
        print(10/x)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid Input")
    finally:
        print("Execution Completed")