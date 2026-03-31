# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1


num  = 5
for i in range(num):
    for j in range(num-i,0,-1):
        print(j,end="")
    print()
    