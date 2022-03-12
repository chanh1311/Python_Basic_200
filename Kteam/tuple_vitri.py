# def tuple_vitri(tupleA, X):
#     tuple_vitri = tuple(i for i in range(len(tupleA)) if tupleA[i] == X)
#     return tuple_vitri


# listA = input().split()
# if len(listA) == 0:
#     print("danh sach rong!")
# else:
#     tupleA = tuple(listA)
#     X = input()
#     if not X:
#         print("X chua co gia tri")
#     else:
#         tuple_vitri = tuple_vitri(tupleA, X)
#         print(tuple_vitri)
########################################
def tim_gia_tri(tupleX, giaTri):
    # Su dung tuple comprehension voi enumerate() de lay ra vi tri cac phan tu giaTri
    tupleViTri = tuple(vt for vt, gt in enumerate(tupleX) if gt == giaTri)
    return tupleViTri


# Nhap tuple tu ban phim
# Su dung Constructor Tuple de khoi tao tuple
tupleX = tuple(input().split())
giaTri = input()

# Goi thuc thi ham va truyen tham so cho ham
ketQua = tim_gia_tri(tupleX, giaTri)

print(ketQua)
