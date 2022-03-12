# c = ["Anh", "Em"]
# d = ["Choi", "Yeu"]
# t = ["Bong Da", "Xep Hinh"]

# for i in c:
#     for j in d:
#         for k in t:
#             print(i, j, k, sep=" ")
##########################
chu_ngu = ["Anh", "Em"]
dong_tu = ["Chơi", "Yêu"]
tan_ngu = ["Bóng đá", "Xếp hình"]
# Code by Quantrimang.com
for i in range(len(chu_ngu)):
    for j in range(len(dong_tu)):
        for k in range(len(tan_ngu)):
            cau = "%s %s %s." % (chu_ngu[i], dong_tu[j], tan_ngu[k])
            print(cau)
