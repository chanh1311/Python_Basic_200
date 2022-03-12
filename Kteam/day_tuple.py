def tao_tuple(n):
    tuple_A = tuple(i for i in range(n))
    return tuple_A


try:
    n = int(input("Nhap n: "))
    assert n >= 0
    tuple_A = tao_tuple(n)
    print(tuple_A)
except AssertionError:
    print("hay nhap so nguyen duong!")
except:
    print("Dinh dang dau vao chua hop le!")
