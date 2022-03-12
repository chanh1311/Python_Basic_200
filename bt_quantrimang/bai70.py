list = [3, 11, 6, 8]
try:
    for x in list:
        assert not x % 2
    print("Day tren chan!")
except AssertionError:
    print("Day tren co it nhat 1 so le!")


##############################
