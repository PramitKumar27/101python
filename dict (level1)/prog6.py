n = input("How big is your dictionary? ")
t = int(n)
dict = {}
for i in range(t):
    a = input("Key: ")
    b = input("Value: ")
    dict[a] = b
    i += 1

print("Dictionary stored..")
a = None
for k, v in dict.items():
    if a is None:
        a = v
    if v < a:
        a = v

print(a)
