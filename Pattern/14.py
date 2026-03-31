# 5 5 5 5 5 
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5
n = 5
for i in range(n):
    for j in range(n-i):
        print("5",end="")
    print()
    
    
# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1


n = 6
for i in range(n - 1):
    for j in range(n - i):
        print(j, end=" ")
    print()
