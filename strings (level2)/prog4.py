str = input("Enter your string: ")
pre = input("Enter your prefix: ")
op = False

n = len(pre)
str1 = str[0:n]
if str1 == pre:
    op = True

print(op)
