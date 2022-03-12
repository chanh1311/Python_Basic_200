def tuple_1to20():
    list_tup = list()
    for x in range(1, 21):
        list_tup.append(x ** 2)

    print(tuple(list_tup))


tuple_1to20()
