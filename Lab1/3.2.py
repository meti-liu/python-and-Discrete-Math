def Cartesianproduct(X, Y):
    result = []
    for x in X:
        for y in Y:
            result.append((x, y))
    return result


X = {1, 2, 3}
Y = {'a', 'b', 'c'}
print(Cartesianproduct(X, Y))
