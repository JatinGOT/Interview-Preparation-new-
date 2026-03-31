#   1
#  22
# 333   

n = 3
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print(i, end="")
    print()


   
#    1
#   22
#  333  

num = 3
for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(i):
        print(i,end="")
        
    print()