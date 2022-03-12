def list_1to20():
    li = list()
    for x in range(1, 21):
        li.append(x ** 2)
    print(li[-5:])


list_1to20()
