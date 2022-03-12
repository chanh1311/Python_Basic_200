# Tao ra 2 list nguyen am, phu am
string = input()
nguyenam = "AEOIU"
stuart = 0
kevin = 0
# Dem so chuoi co the duoc tao ra
for x in range(len(string)):
    if string[x] in nguyenam:
        kevin += len(string) - x
    else:
        stuart += len(string) - x
if stuart > kevin:
    print("Stuart", stuart)
elif stuart < kevin:
    print("Kevin", kevin)
else:
    print("Draw")
