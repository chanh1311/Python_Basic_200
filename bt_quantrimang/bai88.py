# array = [[[0 for col in range(8)] for col in range(5)] for row in range(3)]
# print(array)
########################################################
for i in range(3):
    for j in range(5):
        print([0 for x in range(8)], end=" ")
    print()
