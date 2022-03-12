def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first, last))


if __name__ == "__main__":
    first_name = input().strip()
    last_name = input().strip()
    print_full_name(first_name, last_name)
