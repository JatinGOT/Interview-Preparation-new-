

x = int(input("Enter a leap year"))
if (x%400==0) or (x%4==0 and x%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")