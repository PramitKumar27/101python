str = input("Enter your string: ")
suf = input("Enter your suffix: ")
op = False

n = len(suf)
m = len(str)

str1 = str[m-n:]

if str1 == suf:
    op = True

print(op)
