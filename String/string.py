string = "Jatin"
print(string[0:-1])
print(string[0:])
print(string[::-1])

print(string[1::2])

print(string[-4:])

print(string[1:-1])

s = "abcdef"
half = len(s)//2
print(s[:half][::-1] + s[half:])
s = "abcdefghijk"
print(s[::3])