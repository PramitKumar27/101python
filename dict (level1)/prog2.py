n = input("How big is your dictionary? ")
t = int(n)
dict = {}
for i in range(t):
    a = input("Key: ")
    b = input("Value: ")
    dict[a] = b
    i += 1

print("Dictionary stored..")

c = input("Enter new key: ")
d = input("Enter new value: ")

if c in dict:
    print("Key already exists..")
    print(dict)
else:
    dict[c] = d
    print("Here is your new dictionary!")
    print(dict)
