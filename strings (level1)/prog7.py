str = input("Enter your string: ")
num = int(input("Enter your number: "))

if str == "":
    print(str)
else:
    print(str[0:num]+str[num+1:])
