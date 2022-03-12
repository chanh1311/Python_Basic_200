def bien_doi_chuoi(s):
    if s.startswith("*") and s.endswith("*"):
        return s.title()
    if s.startswith("-") and s.endswith("-"):
        return s.swapcase()

    return s.capitalize()


s = input()
print(bien_doi_chuoi(s))
