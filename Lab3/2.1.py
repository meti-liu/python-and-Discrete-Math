import networkx as nx
import matplotlib.pyplot as plt


def isGraph(V, E):
    for edge in E:
        if edge[0] not in V or edge[1] not in V:
            return False
    return True


def isSubGraph(V, E, Vs, Es):
    if not isGraph(Vs, Es):
        return False
    for v in Vs:
        if v not in V:
            return False
    for e in Es:
        if e not in E:
            return False
    return True


def isProperSubGraph(V, E, Vs, Es):
    if not isSubGraph(V, E, Vs, Es): return False
    if Vs == V and E == Es: return False
    return True


def isSpanningSubGraph(V, E, Vs, Es):
    if not isSubGraph(V, E, Vs, Es):
        return False
    return Vs == V


def isInducedSubGraph(V, E, Vs, Es):
    if not isSubGraph(V, E, Vs, Es):
        return False

    # 检查 Vs 中的每一对顶点
    for v1 in Vs:
        for v2 in Vs:
            if v1 != v2:
                edge_in_original = (v1, v2) in E or (v2, v1) in E
                edge_in_subgraph = (v1, v2) in Es or (v2, v1) in Es

                # 如果 v1 和 v2 在原图中有边，但在子图中没有边，返回 False
                if edge_in_original and not edge_in_subgraph:
                    return False
    return True


def drawGraph(E):
    G = nx.Graph()
    G.add_edges_from(E)
    pos = nx.spring_layout(G)
    options = \
        {
            "font_size": 36,
            "node_size": 3000,
            "node_color": "red",
            "edge_color": "blue",
            "linewidths": 5,
            "font_color": "white",
            "width": 5,
        }
    plt.figure(figsize=(8, 6))
    plt.title("Undirected Graph")
    nx.draw_networkx(G, pos, **options)
    plt.show()


V = {'a', 'b', 'c', 'd', 'e'}
E = {('b', 'c'), ('a', 'c'), ('a', 'b'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'),
     ('c', 'e'), ('b', 'e'), ('d', 'e')}
tv = isGraph(V, E)

drawGraph(E)

print('判断图', tv)
Vs = {'a', 'b', 'c', 'd', 'e'}
Es = {('b', 'c'), ('a', 'c'), ('a', 'b'), ('a', 'd'), ('a', 'e'), ('b', 'd'),
      ('c', 'e'), ('b', 'e'), ('d', 'e')}
tv = isSubGraph(V, E, Vs, Es)

drawGraph(E)

print('判断子图', tv)
tv = isProperSubGraph(V, E, Vs, Es)

drawGraph(E)

print('判断真子图', tv)
Vs = {'a', 'b', 'c', 'd', 'e'}
Es = {('a', 'd'), ('a', 'c'), ('b', 'd'), ('c', 'e'), ('b', 'e')}
tv = isSpanningSubGraph(V, E, Vs, Es)
print('判断生成子图', tv)
Vs = {'a', 'b', 'c', 'e'}
Es = {('b', 'c'), ('a', 'b'), ('a', 'c'), ('a', 'e'), ('c', 'e'), ('b', 'e')}
tv = isInducedSubGraph(V, E, Vs, Es)
print('判断导出子图', tv)
