list1 = [5,4,3,2,1]
n = len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if(list1[j]>list1[j+1]):
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
print("Sorted List ",list1) 