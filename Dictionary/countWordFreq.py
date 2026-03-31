# sentence = "python is easy and python is powerful"
# words = sentence.split()
# freq = {}
# for i in words:
#     if i in freq:
#         freq[i] +=1
#     else:
#         freq[i] = 1
# print(freq)


sentence = "python is easy and python is powerful"
words = sentence.split()
dict = {}
print(words)

for i in words:
    if i in dict :
        dict[i] +=1
    else:
        dict [i]=1
print(dict)


