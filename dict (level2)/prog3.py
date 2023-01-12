my_dict = {
    "a": [1, 2, 3],
    "b": [4, 0, -4],
    "c": [3, 5, 9],
    "d": [45, 12, 100]
}
c = None
for k, v in my_dict.items():
    a = my_dict[k]
    b = sum(a)
    if c is None:
        c = b
    if b > c:
        c = b

print(c)
