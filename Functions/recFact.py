def factorial_number(n=5):
    if n == 1:
        return 1
    return n*factorial_number(n-1)
print(factorial_number())