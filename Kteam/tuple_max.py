def max_tuple(tupleA):
    count = len(tupleA)
    max_item = tupleA[0]
    min_item = tupleA[0]
    for i in tupleA:
        if i > max_item:
            max_item = i
        elif i < min_item:
            min_item = i
    return max_item, min_item, count


tuple_A = input().split()
if len(tuple_A) == 0:
    print("danh sach rong!")
else:
    try:
        tuple_nguyen = tuple(map(float, tuple_A))

        count, max_item, min_item = max_tuple(tuple_nguyen)
        print(count)
        print(max_item)
        print(min_item)
    except:
        print("Dinh dang dau vao khong hop le!")
