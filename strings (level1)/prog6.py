str = input("Enter your string: ")
bool = False
for i in range(len(str)):
    if str[i].isdigit() == True:
        bool = True
        break
    else:
        bool = False

print(bool)
