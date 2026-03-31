text = "Python"
dict1 = {}
for i in text:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)




