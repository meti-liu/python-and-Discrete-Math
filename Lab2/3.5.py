def Ixset(R):
    elements = set()
    for (x, y) in R:
        elements.add(x)
        elements.add(y)
    return {(x, x) for x in elements}


def isreflexive(X,R):
    if Ixset(R) <= R:
        return True
    else:
        return False


def issymmetric(X, R):
    flag = True
    for (a, b) in R:
        if (b, a) not in R:
            flag = False
        else:
            continue
    return flag