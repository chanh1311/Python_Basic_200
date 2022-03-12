def tuple_Chan():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    list_tup = list(tup)
    for x in tup:
        if x % 2 != 0:
            list_tup.remove(x)

    print(tuple(list_tup))


tuple_Chan()
