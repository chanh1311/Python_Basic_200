import re

email = input()
dinh_dang = "(\w+)@(\w+)\.(com)"
# --> (abc)@(abc)(a1!.)(com)
s = re.search(dinh_dang, email)
print(s)
print(s.group(2))
