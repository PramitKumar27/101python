n = input("How big is your dictionary? ")
t = int(n)
dict = {}
for i in range(t):
    a = input("Key: ")
    b = input("Value: ")
    dict[a] = b
    i += 1

print("Dictionary stored..")

dict1 = {}

for k, v in dict.items():
    dict1[v] = dict1.get(v, 0)+1

print(dict1)
