str = input("Enter string: ")
str1 = str.lower()
vowel1 = ['a', 'e', 'i', 'o', 'u']


def vowel(str):
    if len(str) == 0:
        return 0
    elif str[len(str)-1] in vowel1:
        return 1 + vowel(str[:-1])
    else:
        return vowel(str[:-1])


print(vowel(str1))
