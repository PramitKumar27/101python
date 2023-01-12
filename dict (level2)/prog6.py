dict = {
    "description": "shoe",
    "price": 4.56,
    "colors": ["green", "blue", "red"],
}

lst = []
i = 0
lst1 = []

for k, v in dict.items():
    lst.append(k)
    lst.append(v)
    lst1.append(lst)
    lst = []
    i += 1

print(lst1)
