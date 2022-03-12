# string_Ascii = "Hello chanh"
# string_unicode = string_Ascii.encode("utf-8")  # Ascii --> unicode
# print(string_unicode)

s = input()
v = s.encode()  # có thể dùng v=s.encode('utf-8') (Dinh dang b'string')
print(v)
