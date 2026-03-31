number  = [1,2,3,4,5]
for i in number:
    print(i*i)


squared = [i*i for i in number]
print(squared)

# Filter 
number  = [1,2,3,4,5,6]
even = [i for i in number if i%2 == 0]
print(even)

# Tranform a textual data
names = [" ALI ", " Sara " , " JOHN"]
cleaned_data = [name.strip().lower() for name in names if name]
print(cleaned_data)

#  Dictionary Comprehension 
items = ["apple","banana","cherry"]
price = [0.6,0.5,0.1]
price_dict = {items[i]:price[i] for i in range(len(items))}
print(price_dict)

# set comprehension 
values = [1, 2, 2, 3, 3, 4]

unique_squares = {x * x for x in values}
print(unique_squares)

# Nested Comprehension 
pairs = [(x,y) for x in [1,2] for y in [3,4]]
print(pairs)


a  = []
for i in  [1,2]:
    for j in  [3,4]:
        a.append((i,j))
        
print(a)