list_tu = [x for x in input("Nhap chuoi: ").split()]
set_tu = set(list_tu)
ket_qua = sorted(set_tu)
print(type(ket_qua))
print(" ".join(ket_qua))
