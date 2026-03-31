# *****
#  ****
#   ***
#    **
#     *

rows = 5
cols = 5
for i in range(rows):
    for j in range(i):
        print(" ",end='')
    for k in range(rows-i):
        print("*",end="")
    print()
    
    
    


for i in range(rows):
    for j in range(i):
        print(" ",end="")
    for k in range(rows-i):
        print("*",end="")
    print()