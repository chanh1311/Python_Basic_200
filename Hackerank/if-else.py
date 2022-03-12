# n = int(input().strip())
# check = {True: "Not Weird", False: "Weird"}

# print(check[n % 2 == 0 and (n in range(2, 6) or n > 20)])


# #########################################################
# n = int(input())

# if n % 2 != 0:
#     print("Weird")
# else:
#     if n >= 2 and n <= 5:
#         print("Not Weird")
#     elif n >= 6 and n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")
##########################################
n = int(input())
if n % 2 == 0 and (n in range(2, 6) or n > 20):
    print("Not Weird")
else:
    print("Weird")
