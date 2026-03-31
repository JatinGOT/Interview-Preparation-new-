#      *
#     **
#    ***
#   ****
#  *****


rows = 5
cols = 5
for i in range(rows):
    for k in range(rows-i):    
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
    
    
    
    
    
    
    
for i in range(rows):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end="")
    print()