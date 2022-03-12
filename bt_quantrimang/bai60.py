import re

string = input()

list_so = re.findall(
    "\d+", string
)  # Lay gia tri dung gia tri so hoac nhiu so dau vao list
print(list_so)
# Tim kiem theo tung tu co khoang trang ok
