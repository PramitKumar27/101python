str = input("Enter a string: ")
str1 = str.lower()
str2 = "abcdefghijklmnopqrstuvwxyz"
ct = 0

str3 = ""
for i in str2:
    flag = 0
    for j in str1:
        if j == i:
            flag += 1
    if flag > 1:
        ct += 1
        str3 += i


print(ct)
print(str3)
