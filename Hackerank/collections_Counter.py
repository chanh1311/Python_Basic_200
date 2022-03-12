from collections import Counter

myList = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
# # dem do lan xuat hien thang nao nhieu nhat se in truoc
# print(Counter(myList))  # day se tao ra doi tuong Counter
# print(Counter(myList).items())  # Tao cac tuple trong list, sap xep theo key
# print(Counter(myList).keys())  # chi lay gia tri key va duoc sap xep
# print(Counter(myList).values())  # Lay gia tri
##################################################
X = int(input())
List = list(map(int, input().split()))
# myList = Counter(List)
N = int(input())
tongtien = 0
for i in range(N):
    key, item = map(int, input().split())
    if List.count(key) > 0:
        List.remove(key)
        tongtien += item
print(tongtien)


# Bài toán tạo với đầu vào là một list, các cặp key-value trong dãy hãy tính tổng của các value khi key có còn trong list #


################################
# nhap
# X = int(input())
# list_shoe = input().split()
# N = int(input())
# sum_money = 0
# # duyet qua day lay key,value
# for x in range(N):
#     key, value = map(int, input().split())
#     # Xu li:
#     if list_shoe.count(key) > 0:
#         list_shoe.remove(key)
#         sum_money += value
# # hienthi
# print(value)
