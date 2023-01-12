my_dict = {
    "a": [4, 3, 2],
    "b": [5, 3, 7],
    "c": [1, 9, 10],
    "d": [3, 4, 1]
}

for k, v in my_dict.items():
    lst = my_dict[k]
    lst.sort()
    my_dict[k] = lst

print(my_dict)
