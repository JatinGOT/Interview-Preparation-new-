def reverse(strings):
    newString = ""
    for char in strings:
        newString = char + newString
    return newString
print(reverse("jatin"))