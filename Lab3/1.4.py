import networkx as nx
import matplotlib.pyplot as plt

def cyclicGraphSet(n):
    G = nx.cycle_graph(n)
    V = list(G.nodes)
    E = list(G.edges)
    return V, E

def drawGraph(E):
    G = nx.Graph()
    G.add_edges_from(E)
    nx.draw(G, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
    plt.show()

# 测试圈图
n = 10
V, E = cyclicGraphSet(n)
drawGraph(E)
print(E)
print(len(E))
