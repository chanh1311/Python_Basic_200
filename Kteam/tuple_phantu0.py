# def tuple_0(tupleA):
#     count_pt = 0
#     count_kitu = 0
#     for i in tupleA:
#         if i == "0":
#             count_pt += 1
#         for j in i:
#             if j == "0":
#                 count_kitu += 1
#     return count_pt, count_kitu


# tupleA = tuple(input().split())
# if len(tupleA) == 0:
#     print("Tuple rong")
# else:
#     tuple_count0 = tuple_0(tupleA)
#     print(tuple_count0)
###############################
def dem_0(tupleX):
    demPtu0 = tupleX.count("0")
    demKyTu0 = [ptu.count("0") for ptu in tupleX]
    return demPtu0, sum(demKyTu0)


# Nhap tuple tu ban phim
# Su dung Constructor Tuple de khoi tao tuple
tupleX = tuple(input().split())

# Goi thuc thi ham va truyen tham so cho ham
dem0 = dem_0(tupleX)

print(dem0)
