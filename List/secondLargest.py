lst = [10, 20, 5, 30, 25]
second = 0
largest = 0
for num in lst:
    if num>largest:
        second = largest
        largest = num
    elif num > second and num!=largest:
        second = num

print(second)