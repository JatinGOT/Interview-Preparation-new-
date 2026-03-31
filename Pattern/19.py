# 1
# 23
# 456
# 78910

num = 4
count = 1
for i in range(1,num+1):
    for j in range(i):
        print(count,end="")
        count +=1
    print()
    
    

# 1
# 3 2
# 6 5 4
# 10 9 8 7
    
    
num = 4
count = 1

for i in range(1, num + 1):
    temp = count + i - 1      # last number of the current row
    for j in range(i):
        print(temp, end=" ")
        temp -= 1
    count += i
    print()
