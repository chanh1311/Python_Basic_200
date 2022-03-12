list_mau = [12, 24, 35, 70, 88, 120, 155]
list_KetQua = [list_mau[i] for i in range(7) if i != 0 and i != 5 and i != 4]
print(list_KetQua)


#######################################
li = [12, 24, 35, 70, 88, 120, 155]
li = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
print(li)
