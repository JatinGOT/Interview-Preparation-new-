def swap(a, b):
    a, b = b, a 
    # 
    return a, b

x, y = swap(10, 20)
print(x, y)


a = 20
b = 10

a = a + b  # a = 30
b = a - b # b = 20
a = a - b # a = 30
print(a)
print(b)  
