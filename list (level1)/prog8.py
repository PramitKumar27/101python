lst = input("Enter a list: ").split()
flag = 0
for i in lst:
    if int(i) > 3:
        flag += 1

print(flag)
