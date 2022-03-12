def nhap():
    information = {}
    n = int(input())
    if n < 2 or n > 5:
        return False
    else:
        i = 0
        while i < n:
            key = input()
            value = float(input())
            information[key] = value
            i += 1
        return information


def get_Name(information):
    list_values = sorted(information.values())  # tao 1 list voi value duoc sx
    min_value = min(list_values)  # lay min trong list_key do
    while min_value == min(list_values):
        list_values.remove(min_value)  # Xoa cac phan tu co gia tri bang min()
    value_result = min(list_values)  # phan tu min thu 2
    for x, y in sorted(information.items()):  # cap gia tri da duoc sx
        if y == value_result:  # neu key bang min thu 2 thi hien thi values
            print(x)


if __name__ == "__main__":
    information = nhap()
    get_Name(information)
# ##################################
# l = []
# second_lowest_names = []
# scores = set()

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     l.append([name, score])
#     scores.add(score)

# second_lowest = sorted(scores)[1]

# for name, score in l:
#     if score == second_lowest:
#         second_lowest_names.append(name)

# for name in sorted(second_lowest_names):
#     print(name, end="\n")
#######################################
if __name__ == "__main__":
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([score, name])

    a.sort()
    print(a)
    b = [i for i in a if i[0] != a[0][0]]
    print(b)
    c = [j for j in b if j[0] == b[0][0]]
    print(c)

    c.sort(key=lambda x: x[1])  # sap xep theo ten
    for i in range(len(c)):
        print(c[i][1])  # lay ten
