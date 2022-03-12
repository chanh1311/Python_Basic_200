# tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# li = list()
# for i in tp:
#     print(tp[-i])
#     print("Vong lap")
#     if tp[-i] % 2 == 0:
#         print(tp[i])
#         li.append(tp[i])
#         print(li)

# tp2 = tuple(li)
# print(tp2)
###################################
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
li = list()
for i in tp:
    if tp[i - 1] % 2 == 0:
        li.append(tp[i - 1])
        tp2 = tuple(li)
print(tp2)
