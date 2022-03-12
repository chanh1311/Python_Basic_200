# # c1
# def swap_case(s):
#     result = ""
#     for x in s:
#         if x.islower():
#             result += x.upper()
#         else:
#             result += x.lower()
#     return result


# if __name__ == "__main__":
#     s = input()
#     result = swap_case(s)
#     print(result)
# c2
def swap_case(s):
    result = "".join(map(str.swapcase, s))
    return result


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
# In hoa chuỗi nhập vào
