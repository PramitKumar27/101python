str3 = input("Enter your string ")
str2 = str3.replace(" ", "")
str1 = "abcdefghijklmnopqrstuvwxyz"
str = str2.lower()

op = False

for i in range(len(str1)):
    for i in range(len(str)):
        if str[i] == " ":
            break
        elif str1[i] in str[i]:
            op = True
            break

print(op)
