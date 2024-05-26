import networkx as nx
import matplotlib.pyplot as plt


def drawGraph(R):
    G = nx.DiGraph()
    G.add_edges_from(R)
    # pos = nx.spring_layout(G)
    nx.draw(G,  node_size=200, node_color='red', with_labels=True, font_color='white', arrows=True)
    plt.show()


R = {('a', 'b'), ('a', 'd'), ('b', 'c'), ('b', 'e'), ('c', 'z'), ('d', 'e'), ('e', 'z')}
drawGraph(R)