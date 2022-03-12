# list_chan = []
# for x in range(1000, 3001):
#     for i in str(x):
#         if int(i) % 2 != 0:
#             break
#     else:
#         list_chan.append(str(x))
# print(",".join(list_chan))
###########################
values = []
for i in range(1000, 3001):
    s = str(i)
    if (
        (int(s[0]) % 2 == 0)
        and (int(s[1]) % 2 == 0)
        and (int(s[2]) % 2 == 0)
        and (int(s[3]) % 2 == 0)
    ):
        values.append(s)
# Bài tập Python 15, Code by Quantrimang.com
print(",".join(values))
