def compare_String(string1, string2):
    if len(string1) > len(string2):
        print(string1)
    elif len(string2) > len(string1):
        print(string2)
    else:
        print(string1 + " 3> " + string2)


string1, string2 = input().split()
compare_String(string1, string2)
