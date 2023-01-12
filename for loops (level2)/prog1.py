n = input("Enter number: ")
numb = int(n)
bool = True
if numb == 0:
    bool = False

for i in range(numb-1, 1, -1):
    print("%d / %d = %d" % (numb, i, numb % i))
    if numb % i == 0:
        bool = False


if bool == False:
    print("Not Prime")
elif bool == True:
    print("Prime")
