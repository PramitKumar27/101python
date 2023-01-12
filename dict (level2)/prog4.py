
list = input("Enter your string: ").split()
list1 = []

for i in list:
    for char in i:
        if char.isalpha():
            c = char.lower()
            list1.append(c)


dict = {}


for j in list1:
    dict[j] = dict.get(j, 0)+1


print(dict)
