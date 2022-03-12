def attrgetter(*items):
    if any(not isinstance(item, str) for item in items):
        raise TypeError("attribute name must be a string")
    if len(items) == 1:
        attr = items[0]

        def g(obj):
            return resolve_attr(obj, attr)

    else:

        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)

    return g


def resolve_attr(obj, attr):
    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj


def itemgetter(*items):
    if len(items) == 1:
        item = items[0]

        def g(obj):
            return obj[item]

    else:

        def g(obj):
            return tuple(obj[item] for item in items)

    return g


# using itemgetter
itemgetter(1)("ABCDEFG")
"B"
itemgetter(1, 3, 5)("ABCDEFG")
("B", "D", "F")
itemgetter(slice(2, None))("ABCDEFG")
"CDEFG"
soldier = dict(rank="captain", name="dotterbart")
itemgetter("rank")(soldier)
"captain"


inventory = [("apple", 3), ("banana", 2), ("pear", 5), ("orange", 1)]
getcount = itemgetter(1)
print(getcount)
list(map(getcount, inventory))
[3, 2, 5, 1]
sorted(inventory, key=getcount)
[("orange", 1), ("banana", 2), ("apple", 3), ("pear", 5)]

# using attrgetter:
import operator


class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b


c = C(1, 2)

getter = attrgetter("a")
print(getter(c))
# OUTPUT
# 1

getter = attrgetter("a", "b")
print(getter(c))
# OUTPUT 1,2
