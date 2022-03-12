from itertools import product


def TongBinhPhuong_List(sum_list, M):
    obj_product = product(
        *sum_list
    )  # Tao raa doi tuong product(chua cac tuple con),product--> nhan cheo cac interable, co the tao 1 list tu doi tuong product cung duoc.
    result = map(
        lambda x: sum(i ** 2 for i in x) % M, obj_product
    )  # Tra ve doi tuong map, truyen lan luot cac tuple vao x sao do xu li ben trong lan luot.
    return result  # doi tuong map cung la interable


def Max_BieuThuc(result):
    max_result = max(
        result
    )  # lay max cua interable la doi tuong map(cac so ben trong la ket qua cua bieu thuc de cho)
    return max_result


# nhap K,M (K la so list,M la so chia)
def nhap():
    K, M = map(int, input().split())
    sum_list = [
        list(map(int, input().split()))[1:] for _ in range(K)
    ]  # tao 1 list cac list duoc nhap vao, lay tu phan tu thu 1#
    return M, sum_list


def main():
    M, sum_list = nhap()
    result = TongBinhPhuong_List(sum_list, M)
    max_result = Max_BieuThuc(result)
    print(max_result)


if __name__ == "__main__":
    main()
