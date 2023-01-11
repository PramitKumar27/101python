dict = {"a": 4, "b": 6}
key = "c"
bool = False
for k, v in dict.items():
    if key in k:
        bool = True

print(bool)
