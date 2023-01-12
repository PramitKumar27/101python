lst = input("Enter the string: ")

v = ['a', 'e', 'i', 'o', 'u']
for i in lst:
    if i.isalpha() == True:
        if i in v:
            print(i, " is a vowel")
        else:
            print(i, " is a consonant")
    else:
        print(i, " is not a letter")
