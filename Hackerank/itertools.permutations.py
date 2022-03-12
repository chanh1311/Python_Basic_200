from itertools import permutations

# hoán vị 1 interable

String, Len = input().split()

list = list(permutations(sorted(String), int(Len)))
print(list)
for x in list:
    print("".join(x))  # da xuong dong

# Hien thi tung phan cua 1 chuoi cach nhau boi xuong hang, chieu dai phần cho trước, có thứ tự
"""
1. Nhập chuỗi và dộ dài của chuỗi
2. Sắp xếp chuỗi và đưa vào hàm permutation để tách chuỗi thành từng phần
3. Hiển thị theo định dạng
"""


############################################
# from itertools import permutations
# s,n = input().split()
# print(*["".join(i) for i in permutations(sorted(s),int(n))])


#################################permutations#####################################
"""
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
"""
