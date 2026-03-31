# 0 1 1 2 3 5 8 13
num = 8

a = 0
b = 1

for temp in range(num):
    print(a , end=" ")
    temp = a  
    a = b
    b = b + temp
    
# temp = 0
# print (0)
# a = b // a = 1
# b = b + temp // 1



# temp = 1
# print (1)
# temp = a // temp = 1
# a = b // a = 1
# b = b + temp // b = 2

# temp = 2
# print (1)

# temp = a // temp = 1
# a = b // a = 2
# b = b + temp // b = 3 

# temp= 3
# print (2)
# temp = a // 2
# a = b // a = 3
# b = b + temp // b = 5

# temp = 4
# print (3)
# temp  = a // a = 3
# a = b // a = 5
# b = b + temp // bb = 8

# num = 2
# for i in range(4):
#     print(num)
#     if i < 2 :
#         num = num*2
#     else :
#         num = num * 4