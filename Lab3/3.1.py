#调用networkx的部分已经注释掉，不会影响矩阵的生成
import random
# import networkx as nx
# import matplotlib.pyplot as plt
def createGraph(m, n): #默认无向图，有向图同理
    V = list(range(m))
    E = set()
    while len(E) < n:
        u = random.choice(V)
        v = random.choice(V)
        E.add((u, v))
    return V, list(E)

def graph2Array(V, E):
    n = len(V)
    A = [[0] * n for _ in range(n)]
    for (u, v) in E:
        A[u][v] = 1
        A[v][u] = 1
    return A


# def drawGraph(E):
#     G = nx.Graph()
#     G.add_edges_from(E)
#     nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=15)
#     plt.show()

def printMatrix(A):
    for row in A:
        print(row)

m, n = 6, 10
V, E = createGraph(m, n)
A = graph2Array(V, E)
# drawGraph(E)
printMatrix(A)