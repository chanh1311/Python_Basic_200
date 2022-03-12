n = int(input())
integer_List = map(int, input().split())
integer_Tuple = tuple(integer_List)
print(hash(integer_Tuple))
