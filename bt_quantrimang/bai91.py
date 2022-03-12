list1 = set([1, 3, 6, 78, 35, 55])
list2 = set([12, 24, 35, 24, 88, 120, 155])

list1 &= list2
print(list1)
list1 = list(list1)
print(list1)
