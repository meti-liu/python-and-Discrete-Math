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


def istransitive(X, R):
    for (a, b) in R:
        for (c, d) in R:
            if b == c and (a, d) not in R:
                return False
    return True


def isequivalent(X, R):
    return issymmetric(X, R) and istransitive(X, R) and isreflexive(X, R)

def equivalence_classes(X, R):
    if isequivalent(X,R)==False:
        print("不是等价关系，无等价类")
    classes=[] #由很多eqclass组成的列表
    seen=set() #已经操作过的等价类

    for x in X: #每个x对应唯一的等价类
        eqclasses=set() #用集合来存储等价类
        for y in X:
            if y not in seen and (x,y) in R:
                eqclasses.add(y)
                seen.add(y)
        if eqclasses!=set():#非空集
            classes.append(eqclasses)
    return classes


X = {'a', 'b', 'c', 'd', 'e', 'f'}
R = {('a', 'b'), ('b', 'a'), ('a', 'a'), ('b', 'b'), ('c', 'c'),
     ('d', 'd'), ('e', 'e'), ('f', 'f'), ('c', 'd'), ('d', 'c')}

print("R 是否为等价关系:", isequivalent(X, R))  # 应返回 True
print("等价类:", equivalence_classes(X,R))