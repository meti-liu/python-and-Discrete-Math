R={(4, 4), (0, 1), (2, 1), (0, 0), (3, 1), (1, 1), (2, 0), (3, 0), (3, 3), (1, 0)}
S={(4, 4), (0, 1), (4, 0), (1, 2), (4, 3), (3, 1), (1, 4), (0, 2), (1, 0), (4, 1)}
print("R∩S",R&S)#或R.union(S)
print("R∪S=",R|S)#或R.intersection(S)
print("R-S=", R.difference(S))#R-S
print("R⊕S=", R.symmetric_difference(S))#R ^ S
def composite(R,S):
    result=set()
    for (a,b) in R:
        for (c,d) in S:
            if b==c: result.add((a,d))
    return  result
print("R∘S=",composite(R,S))

def Ixset(R):
    elements=set()
    for (x, y) in R:
        elements.add(x)
        elements.add(y)
    return {(x, x) for x in elements}

def power(R,n):
    if n==0:
        return Ixset(R)
    elif n==1:
        return R
    else:
        return composite(R,power(R,n-1))
n=int(input("输入n"))
print("R^",n,"=",power(R,n))