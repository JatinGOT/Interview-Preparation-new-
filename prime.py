num = int(input("Enter a number : "))

isPrime = True

for i in range(2,num):
    if (num%2==0):
        isPrime = False
    
print(isPrime)