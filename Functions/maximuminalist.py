

def findmax(lst):
    max_lst = lst[0]
    for i in lst:
        if i>max_lst:
            max_lst = i
    return max_lst
                
print(findmax([1,2,3,45,5]))
        