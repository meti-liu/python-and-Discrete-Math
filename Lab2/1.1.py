import random


def Cartesianproduct(X, Y):
    result = []
    for x in X:
        for y in Y:
            result.append((x, y))
    return result


X = {1, 2, 3, 4}
Y = {'a', 'b', 'c'}

R = random.sample(Cartesianproduct(X, Y), 6)
print(R)
