data = {"a": 1, "b": 2, "c": 1, "d": 3}
unique = {}
seen = []
for key,value in data.items():
    if value not in seen:
        unique[key] = value
        seen.append(value)
print(unique)



data = {"a": 1, "b": 2, "c": 1, "d": 3}
unique = {}
seen = []
for key,value in data.items():
    if value not in seen:
        unique[key] = value
        seen.append(value)
        
print(unique)