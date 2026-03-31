lst = [1, 2, 2, 3, 1, 4, 2]
freq = {}
for item in lst:
    if item in freq:
        freq[item] +=1
    else:
        freq[item] = 1
print(freq)