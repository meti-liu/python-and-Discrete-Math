def Ixset(R):
    a = []
    for x in R:
        a.append((x, x))
    a.sort()
    return a


def Uxset(R):
    a = []
    for x in R:
        for y in R:
            a.append((x, y))
    a.sort()
    return a


x1 = set(range(20))
x2 = set(range(8))
print(Ixset(x1))
print(Uxset(x2))
