# def so_Chan(number):
#     if number % 2 == 0:
#         return True
#     return False


def loc_Ds():
    list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_number_new = filter(lambda x: x % 2 == 0, list_number)
    return list_number_new


list_number = loc_Ds()
print(list(list_number))
