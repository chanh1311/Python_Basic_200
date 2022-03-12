# from typing import List


# list_Mau = [12, 24, 35, 70, 88, 120, 155]

# list_Mau = [x for i, x in enumerate(list_Mau) if i == 1 or i == 3 or i == 5]
# print(list_Mau)
#################################
li = [12, 24, 35, 70, 88, 120, 155]
# Code by Quantrimang.com
a = [x for i, x in enumerate(li) if i % 2 != 0]
print(a)
