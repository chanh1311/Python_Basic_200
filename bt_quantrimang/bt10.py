# M, N = map(int, input().split())
# for i in range(M):
#     for j in range(N):
#         print(i * j, end=" ")
#     print()
#########################
output = []
M, N = map(int, input().split(","))
for i in range(M):
    dong = [i * j for j in range(N)]
    output.append(dong)
print(output)
########################
# input_str = input("Nhập X, Y: ")
# dimensions = [int(x) for x in input_str.split(",")]
# rowNum = dimensions[0]
# colNum = dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# print(multilist)
# # Viết bởi Quantrimang.com
# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col] = row * col

# print(multilist)
