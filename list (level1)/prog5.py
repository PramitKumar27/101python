lst = input("Enter your list: ").split()
a = 0
if lst == []:
    print("Empty List")
else:
    for i in lst:

        print(i, a)
        a += 1
