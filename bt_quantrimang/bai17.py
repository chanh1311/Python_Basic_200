string = input()
d = {"UPPER": 0, "LOWER": 0}
for x in string:
    if x.islower():
        d["LOWER"] += 1
    elif x.isupper():
        d["UPPER"] += 1
    else:
        pass
print("Phần tử in hoa la:", d["UPPER"])
print("Phần tử in thường là:", d["LOWER"])
