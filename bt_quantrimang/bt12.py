list_upper = []
while True:
    s = input()
    if s:
        list_upper.append(s.upper())
    else:
        break

for x in list_upper:
    print(x)
