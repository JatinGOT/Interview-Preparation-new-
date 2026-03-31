def get_even_numbers(lst):
    even_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

print(get_even_numbers([1, 2, 3, 4, 5, 6]))
