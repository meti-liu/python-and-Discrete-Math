import networkx as nx
import matplotlib.pyplot as plt

def createGraph(m, n):
    G = nx.gnm_random_graph(m, n)
    V = list(G.nodes)
    E = list(G.edges)
    return V, E

def drawGraph(E):
    G = nx.Graph()
    G.add_edges_from(E)
    nx.draw(G, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
    plt.show()

# 测试无向图
m, n = 10, 20
V, E = createGraph(m, n)
drawGraph(E)
print(E)
print(len(E))
