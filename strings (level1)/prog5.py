str = input("Enter a string: ")
str1 = ""
n = len(str)
i = 0
if n < 2:
    print(str)
else:
    while i < n:
        if i % 2 != 0:
            str1 = str1+str[i]
        i = i+1
    print(str1)
