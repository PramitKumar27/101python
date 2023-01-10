str = input("enter a string: ")
str1 = ""
n = len(str)

if n == 0:
    print("")
else:
    while n > -1:
        str1 = str1+str[n-1]
        n = n-1
    print("reversed string: ", str1)
