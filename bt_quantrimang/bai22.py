# list_tuple_name = []
# while True:
#     string = input()
#     if not string:
#         break
#     else:
#         tuple_name = tuple(string.split(","))
#         list_tuple_name.append(tuple_name)
# list_sapxep_name = sorted(list_tuple_name)

# print(list_sapxep_name)

from operator import itemgetter, attrgetter

# Bài tập Python 22 Code by Quantrimang.com
l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0, 1, 2)))  # sap xep theo thu tu 0 1 2
# print(itemgetter(0, 1, 2))
