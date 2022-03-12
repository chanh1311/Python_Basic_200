# # Nhap n
# n = int(input())

# # # Nhap cac bieu thuc
# List = []
# for _ in range(n):
#     List.append(input().split())

# result = []
# for x in range(n):
#     if List[x][0] == "insert":
#         result.insert(int(List[x][1]), int(List[x][2]))
#     elif List[x][0] == "print":
#         print(result)
#     elif List[x][0] == "remove":
#         result.remove(int(List[x][1]))
#     elif List[x][0] == "append":
#         result.append(int(List[x][1]))
#     elif List[x][0] == "sort":
#         result.sort()
#     elif List[x][0] == "pop":
#         result.pop()
#     elif List[x][0] == "reverse":
#         result.reverse()
########################################
n = int(input())
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    print(cmd)
    args = s[1:]
    print(args)
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        # print(cmd)
        eval("l." + cmd)
    else:
        print(l)

################################################
"""
1. Nhập n số câu lệnh tối đa, tạo 1 list rỗng
2. Mỗi 1 dòng lấy từng câu lệnh và đối số phía sau
3. Nếu not print thì tạo ra cấu trúc câu lệnh thêm vào l  bởi eval để chạy
4. Ngược lại thì hiển thị list

"""
