lst = [5,4,3,2,1]
print(lst[::-1])

reverse =[]
for i in lst:
    reverse =[i] + reverse
print(reverse)

