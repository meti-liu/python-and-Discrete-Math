import networkx as nx
import matplotlib.pyplot as plt

def Ixset(R):
    elements = set()
    for (x, y) in R:
        elements.add(x)
        elements.add(y)
    return {(x, x) for x in elements}


def isirreflexive(X,R):
    if Ixset(R)&R==set():#交集为空集
        return True
    else:
        return False

def isantisymmetric(X,R):
    for (a,b) in R:
        if a!= b and (b,a) in R: return False
    return True

def istransitive(X ,R):
    for(a , b) in R:
        for (c , d) in R:
             if b==c and (a,d) not in R:
                return False
    return True

def ispartial(X,R):
    return isantisymmetric(X,R) and isirreflexive(X,R) and istransitive(X,R)

def Hasse(X,R):
    if ispartial(X,R)==False:
        print("不是偏序关系，无法构建哈斯图")
    R=set(R)#显示声明R为集合
    H = R.copy()
    for(a,b) in R:
        for (c,d) in R:
            if b==c and (a,d) in H:
                H.remove((a,d))
    return H

def DrawDiagram(R):
    G = nx.DiGraph()
    G.add_edges_from(R)
    # pos = nx.spring_layout(G) 单方向排列
    nx.draw(G, with_labels=True, node_size=2000, node_color='skyblue', font_size=16, font_weight='bold')
    plt.title("Hasse Diagram")
    plt.show()


X = {'a', 'b', 'c', 'd'}
R = {('a', 'b'), ('b', 'c'), ('a', 'c'), ('c', 'd'), ('a', 'd'), ('b', 'd')}

print("R 是否为偏序关系:", ispartial(X,R))

print("哈斯图关系H:", Hasse(X, R))

DrawDiagram(Hasse(X, R))
