# chuoinhap = input().split(",")
# tam = None
# for i in range(len(chuoinhap)):
#     for j in range(i + 1, len(chuoinhap)):
#         if chuoinhap[j][0] < chuoinhap[i][0]:
#             tam = chuoinhap[j]
#             chuoinhap[j] = chuoinhap[i]
#             chuoinhap[i] = tam
# print(",".join(chuoinhap))
###########################
list_ten = [x for x in input("Nhap chuoi: ").split(",")]
list_ten.sort()
print(",".join(list_ten))
