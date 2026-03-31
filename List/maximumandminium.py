lst = [10, 5, 20, 8]
max = lst[0]
min = lst[0]

for num in lst:
    if num>max:
        max = num
    if num < min:
        min = num

print("Maximum ", max)
print("Minium ", min)