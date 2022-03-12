def tuple_n(n):
    tuple_con = tuple(n for i in range(n))
    tuple_ketqua = (n, tuple_con)
    return tuple_ketqua


try:
    n = int(input())
    assert n >= 0
    tuple_A = tuple_n(n)
    print(tuple_A)
except AssertionError:
    print("Sai dinh dang dau vao!")
except:
    print("Sai dinh dang dau vao!")
