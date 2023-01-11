
dict = {}
for i in range(3):
    a = input("Key: ")
    b = input("Value: ")
    dict[a] = b
    i += 1
print("2nd dict")
dict1 = {}
for i in range(3):
    a = input("Key: ")
    b = input("Value: ")
    dict1[a] = b
    i += 1
print("Dictionaries stored..")
final_dict = {}
for k, v in dict.items():
    final_dict[k] = v

for k, v in dict1.items():
    final_dict[k] = v

print(final_dict)
