a = input("Enter string : ")
b = input("Enter string : ")


def two_string(a, b):
    if len(a) == len(b):
        print(a)
        print(b)
    elif len(a) > len(b):
        print(a)
    else:
        print(b)


two_string(a, b)
