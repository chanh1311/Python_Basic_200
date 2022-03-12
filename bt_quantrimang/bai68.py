# n = int(input())
# list_chan = []
# for x in range(0, n + 1):
#     if not x % 2:
#         list_chan.append(str(x))

# print(",".join(list_chan))


def generator(n):
    i = 0
    while i <= n:
        if not i % 2:
            yield i  # tra ve vi tri nay

        i += 1  # bat dau lan goi moi se tai vi tri nay


list_giatri = []
n = int(input())
for x in generator(n):
    list_giatri.append(str(x))

print(",".join(list_giatri))
