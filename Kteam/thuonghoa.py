def chuyen_doi_chuoi(s):
    if len(s) == 0:
        return ""
    if s[0].islower():
        return s.lower()
    if s[0].isupper():
        return s.upper()
    else:
        return s


print("Nhap vao chuoi s:")
s = input()
print(chuyen_doi_chuoi(s))
