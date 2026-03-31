# 333 
#  22
#   1

num = 3
for i in range(3):
    # print spaces
    for s in range(i):
        print(" ",end = "")
    
    for j in range(num - i):
        print(num-i,end="")
        
    print()
    



# 333 
#  22 
#   1
  
  
num = 3
for i in range(num):
    for j in range(i):
        print(" ",end="")
    
    for k in range(num-i):
        print(num-i,end="")
    print()
    