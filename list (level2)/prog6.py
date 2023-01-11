lst = input("Enter your list: ").split()
dict0 = dict()

for i in lst:
    if i in dict0:
        dict0[i] += 1
    else:
        dict0[i] = 1

print(dict0)
