# from collections import defaultdict

# d = defaultdict(list)
# list1 = []
# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     d[input()].append(str(i))
# for j in range(0, m):
#     list1.append(input())
# for i in list1:
#     if i in d.keys():
#         print(" ".join(map(str, d[i])))
#     else:
#         print(-1)
#########################################
# from collections import defaultdict

# # # nhap, khai bao defaultdict
# n, m = list(map(int, input().split()))
# d = defaultdict(list)
# print(d)
# # nhap key va gan value dua vao dict
# for i in range(n):
#     d[input()].append(i + 1)


# # nhap key tim value trong dict
# for i in range(m):
#     print(*d[input()] or -1)
# print([] or -1)--> -1
##################################


from collections import defaultdict

# nhap va khai nao defaultdict
M, N = map(int, input().split())
d = defaultdict(list)  # value se co 1 tap list
print(d)
# Nhap va gan gia tri cho key value
for i in range(M):
    d[input()].append(i + 1)
    print(d)
# Duyet qua tung phan tu can lay values
for j in range(N):
    print(*d[input()] or [-1])


# Bài toán nhap vao 1 day lon va gan vi tri cho no, nhan vao day nho tra ve vi trị của từng phần tử dãy nhỏ trùng với vị trí trong dãy lớn #
# 1. Nhập vào 2 số M,N
# 2. Tạo ra 1 defaultdict(list)--> 1 dict chứa list bên trong là các value
# cho vong vap chạy qua dãy lớn và gán vị trí
# Duyệt từng phần tử trong dãy nhỏ tùng với dãy lớn và hiển thị value của chúng là những giá trị
