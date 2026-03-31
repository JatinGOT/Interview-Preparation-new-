# rows = 5
# cols = 5
# for i in range(rows):
#     for s in range(rows-i-1):
#         print(" ",end="")
#     for j in range(2*i+1):
#         print("*",end="")
#     print()
# for i in range(1,rows):
#     for s in range(i):
#         print(" ",end="")
#     for j in range(2*(rows-i)-1):
#         print("*",end="")    
#     print()
    
    
    


rows = 5
cols = 5
for i in range(rows):
    for j in range(rows-i-1):
        print(" ",end="")
    
    for k in range(2*i+1):
        print("*",end="")
    print()


for i in range(1,rows):
    for j in range(i):
        print(" ",end="")
    
    for k in range(2*(rows-i)-1):
        print("*",end="")
    print()


